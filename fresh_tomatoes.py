import webbrowser
import os
import re

# <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
# <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
#     # <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Spectre CSS -->
    <link rel="stylesheet" href="spectre.min.css">
    <link rel="stylesheet" href="font-awesome-4.7.0/css/font-awesome.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>

    <style type="text/css" media="screen">
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            text-align: center;
            margin: 20px;
            padding-top: 20px;
        }
        .poster {
            margin: 10px auto;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-overlay, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
            $("#trailer-video-name").empty();
            $("#trailer").removeClass('active');
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id');
            var trailerName = $(this).attr('data-trailer-name');
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
            $("#trailer-video-name").empty().append(trailerName);
            $("#trailer").addClass('active');
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body class="container">
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
        <div class="modal-overlay"></div>
        <div class="modal-container">
            <div class="modal-header">
                <button class="btn btn-clear float-right hanging-close" data-dismiss="modal"></button>
                <div class="modal-title" id="trailer-video-name">Modal title</div>
            </div>
            <div class="modal-body">
                <div class="content">
                    <div class="scale-media" id="trailer-video-container" class="video-responsive">
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button data-dismiss="modal" class="btn btn-link hanging-close">Close</button>
                <button class="btn btn-primary">Share</button>
            </div>
        </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
    <header class="navbar">
        <section class="navbar-section">
                <h1><i class="fa fa-film"></i> Fresh Tomatoes</h1>
        </section>
    </header>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="card col-xs-12 col-sm-6 col-md-4 col-lg-3 col-xl-2 column col-2 movie-tile" data-trailer-youtube-id="{trailer_youtube_url}" data-trailer-name="{movie_title}" data-toggle="modal" data-target="#trailer">
    <div class="card-image" >
        <img src="{poster_image_url}" class="img-responsive poster" width="220" height="342"/>
    </div>
    <div class="card-header">
        <h4 class="card-title">{movie_title}</h4>
        <h6 class="card-meta">Movie Type</h6>
    </div>
    <div class="card-body">
        To make a contribution to the world by making tools for the mind that advance humankind.
    </div>
</div>

'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = '<div class="columns">'
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_url = (youtube_id_match.group(0) if youtube_id_match
                               else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image,
            trailer_youtube_url=trailer_youtube_url
        )
    content += '</div>'
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)

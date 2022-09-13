import youtube_dl, youtube_search
import wget
import os


def get_image(query):
    results = youtube_search.YoutubeSearch(query, max_results=1).to_dict()
    # get thumbnail from youtube for query
    url = "https://www.youtube.com" + results[0]["url_suffix"]
    with youtube_dl.YoutubeDL({'quiet': True}) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        thumbnail = info_dict.get('thumbnail', None)
        # download thumbnail
        # if thumbnail.jpg exists, delete it
        if os.path.exists("cache/thumbnail.jpg"):
            os.remove("cache/thumbnail.jpg")
        wget.download(thumbnail, out="cache/thumbnail.jpg")
# download youtube videos as mp3
import youtube_dl
import youtube_search

def download(query):
    # download to cache folder
    results = youtube_search.YoutubeSearch(query, max_results=1).to_dict()
    suffix = results[0]["url_suffix"]
    url = "https://www.youtube.com" + suffix
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'cache/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    # return file path
    return "cache/" + results[0]["title"] + ".wav"
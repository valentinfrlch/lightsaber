# download youtube videos as mp3
import youtube_dl
import youtube_search

def download(url):
    # download to cache folder
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
      
        
def get_first_result(query):
    # get first result from youtube search
    results = youtube_search.YoutubeSearch(query, max_results=1).to_dict()
    suffix = results[0]["url_suffix"]
    url = "https://www.youtube.com" + suffix
    return url

download(get_first_result("I Ain't worried"))
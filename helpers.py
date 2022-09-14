import youtube_dl, youtube_search
import wget
import os
import librosa
import matplotlib.pyplot as plt
import librosa.display


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
        

def visualizer(file_path):
    """
    visualize audio file as a waveform
    """
    # load audio file
    y, sr = librosa.load(file_path, mono=True)
    # get beats
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    # convert all beats from frames to seconds
    beats = librosa.frames_to_time(beats, sr=sr).tolist()
    # convert tempo from bpm to seconds
    tempo = 60/tempo
    # visualize audio file as a waveform
    plt.figure(figsize=(20, 8))
    librosa.display.waveshow(y, sr=sr)
    # plot beats
    plt.vlines(beats, -1, 1, color='r')
    # hide the axis and the frame
    plt.axis('off')
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    # save plot
    plt.savefig("cache/visualizer.png")
    plt.close()
    return "cache/visualizer.png"
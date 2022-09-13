# analyze beats from mp3 files

import librosa
import ffmpeg


def prepare_audio(file_path):
    #convert to wav with python-ffmpeg
    stream = ffmpeg.input(file_path)
    new_file_name = file_path.replace(".mp3", ".wav")
    stream = ffmpeg.output(stream, new_file_name)
    ffmpeg.run(stream)
    return new_file_name

def get_beats(file_path):
    if file_path.endswith(".mp3"):
        file_path = prepare_audio(file_path)
    # convert mp3 to wav
    y, sr = librosa.load(file_path, mono=True)
    # get beats
    global tempo
    global beats
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    tempo = 60/tempo
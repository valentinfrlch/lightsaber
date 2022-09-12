# analyze beats from mp3 files

import librosa
import os
import ffmpeg


def prepare_audio(file_path):
    #convert to wav with python-ffmpeg
    stream = ffmpeg.input(file_path)
    stream = ffmpeg.output(stream, "cache/test.wav")
    ffmpeg.run(stream)
    return "cache/test.wav"

def get_beats(file_path):
    # convert mp3 to wav
    y, sr = librosa.load(file_path, mono=True)
    # get beats
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    tempo = 60/tempo
    return tempo, beats


path = "C:\\Users\\valen\Documents\\dev\\lightsaber\\test.mp3"
get_beats(prepare_audio(path))

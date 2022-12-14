# analyze beats from mp3 files

import librosa
import ffmpeg
import os
import numpy as np


def prepare_audio(file_path):
    #convert to wav with python-ffmpeg
    stream = ffmpeg.input(file_path)
    new_file_name = file_path.replace(".mp3", ".wav")
    stream = ffmpeg.output(stream, new_file_name)
    ffmpeg.run(stream)
    return new_file_name


# compare sound spectogram to a database of sounds
# figure out which sound it is 

def compare(y, sr):
    """
    compare sound spectogram to a database of sounds
    figure out which sound it is 
    ------------------------------------------------
    y, sr: audio file; generated by librosa
    sounds: list of sounds to compare to; (.wav)
    """
    # load the sound library
    sounds = []
    for file in os.listdir("sounds"):
        sounds.append(file)
    
    # get spectogram of audio snippet
    spec = librosa.feature.melspectrogram(y=y, sr=sr)
    # get the most similar sound
    best_sound = None
    best_score = 0
    for sound in sounds:
        # get spectogram of sound
        y, sr = librosa.load("sounds/" + sound, mono=True)
        sound_spec = librosa.feature.melspectrogram(y=y, sr=sr)
        # compare spectograms
        score = np.sum(np.abs(spec - sound_spec))
        # if this is the best score, save the sound
        if score < best_score:
            best_score = score
            best_sound = sound
    # return the best sound
    return best_sound.replace(".wav", "")



def analyze_beats(beats, tempo, file_path):
    beat_types = []
    for beat in beats:
        # get a 0.5 second audio snippet from the audio file
        y, sr = librosa.load(file_path, offset=beat, duration=tempo)
        beat_type = compare(y, sr)
        beat_types.append(beat_type)
    return beat_types

def get_beats(file_path):
    if file_path.endswith(".mp3"):
        file_path = prepare_audio(file_path)
    # convert mp3 to wav
    y, sr = librosa.load(file_path, mono=True)
    # get beats
    global tempo
    global beats
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    # convert all beats from frames to seconds
    beats = librosa.frames_to_time(beats, sr=sr).tolist()
    tempo = 60/tempo
    beat_types = analyze_beats(beats, tempo, file_path)
    return tempo, beats
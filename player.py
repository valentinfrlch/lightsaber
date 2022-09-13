from re import S
import threading
import time, os
import analyzer as ay
def main(file_path, beats):
    # play audio at file_path
    s = threading.Thread(target=play, args=(file_path,))
    s.start()
    b = threading.Thread(target=interpret_beats, args=(beats,))
    b.start()
    s.join()
    b.join()
    
    
def play(file_path):
    # play audio at file_path with ffmpeg
    command = "ffplay -nodisp -autoexit -hide_banner -loglevel panic " + file_path
    os.system(command)


def interpret_beats(beats):
    # start a timer and play a sound at each beat
    beat_diff = 0
    for beat in beats:
        print("###############################################")
        # get difference between this and the next beat
        beat_diff = beats[beats.index(beat) + 1] - beat
        time.sleep(beat_diff)
        os.system("cls")
      
      
tempo, beats = ay.get_beats("cache/test.wav")
main("cache/test.wav", beats)
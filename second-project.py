import numpy as np
import simpleaudio as sa

# Common sampling frequency
sample_rate = 44100 
# White keys are in Uppercase and black keys (sharps) are in lowercase (Piano)
notes = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B'] 
# https://www.aviom.com/blog/all-about-eq-part-1/
base_frequencies = [16.35, 32.7, 65.41, 130.8, 261.6, 523.3, 1047, 2093, 4186] # Frequency of Note C
# https://en.wikipedia.org/wiki/Dotted_note
augmentation_dot = [1, 1.5, 1.75, 1.875, 1.9375]
# defining a function for generating a single note wave
def generate_wave(frequency, duration):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(2 * np.pi * frequency * t)
    return wave
# getting user musical note
music_notes = input('Enter the musical note:\n').split() 
music_waves = []
for i in range(0, len(music_notes)):
    [d, c, a, b] = list(music_notes[i])
    duration = augmentation_dot[int(d)]*(1/pow(2,int(c)))
    if a=='S':
        frequency = 0 # silent note
    else:
        frequency = base_frequencies[int(b)] * pow(2,(notes.index(a)/12))
    music_waves.append(generate_wave(frequency, duration))

# concatenate notes
audio = np.hstack(music_waves)
# normalize to 16-bit range
audio *= 32767 / np.max(np.abs(audio))
# convert to 16-bit data
audio = audio.astype(np.int16)
# start playback
play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
# wait for playback to finish before exiting
play_obj.wait_done()
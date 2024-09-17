import simpleaudio as sa


def play_sound(filename):
    track = sa.WaveObject.from_wave_file(filename)
    track.play()


from pydub import AudioSegment
from pydub.generators import Sine

def generate_note(frequency, duration=1000):
    # 生成一秒钟的正弦波音符
    sine_wave = Sine(frequency)
    audio = sine_wave.to_audio_segment(duration=duration)
    return audio

def midi_to_frequency(midi_note):
    return 440.0 * (2.0 ** ((midi_note) / 12.0))

import simpleaudio as sa

def play_chords(chords):
    for chord in chords:
        notes = []
        for note in chord:
            frequency = midi_to_frequency(note)  # 将数字转换为MIDI音符
            audio = generate_note(frequency)
            audio = audio.raw_data  # 获取原始音频数据
            play_obj = sa.play_buffer(audio, num_channels=1, bytes_per_sample=2, sample_rate=44100)
            notes.append(play_obj)
        for note in notes:
            note.wait_done()  # 等待和弦中的所有音符播放完成

import re

def parse_chords(input_string):
    chord_pattern = re.compile(r'\((\d+)\)')
    chords = chord_pattern.findall(input_string)
    return [[int(note) for note in str(chord)] for chord in chords]

# 主程序
if __name__ == "__main__":
    input_string = "(111)(333555)"
    chords = parse_chords(input_string)
    play_chords(chords)

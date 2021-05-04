import wave

def frame_rate_channel(audio_file_name):
    with wave.open(audio_file_name, 'rb') as wave_file:
        frame_rate = wave_file.getframerate()
        channels = wave_file.getnchannels()
        return frame_rate, channels
from initial_setup import *
from google_transcribe import google_transcribe
from write_transcripts import write_transcripts
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\Projects\Python\speech\GoogleKeys.json"
filepath="./data/audio/"
output="./data/text/"

if __name__ == '__main__':
    for audio_file_name in os.listdir(filepath):
        transcript = google_transcribe(audio_file_name)
        transcript_filename = audio_file_name.split('.')[0] + '.txt'
        write_transcripts(transcript_filename, transcript)
bucketname = "speech-lab-bucket"

from pydub import AudioSegment
import io
import os
import wave
from google.cloud import speech, storage

#enums and types directly from speech
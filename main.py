#!/usr/bin/env python3

import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
from os import path

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)),
                       "Video_test_1.wav")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
  audio = r.record(source)  # read the entire audio file

# recognize speech using Google Speech Recognition
try:
  # for testing purposes, we're just using the default API key
  # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
  # instead of `r.recognize_google(audio)`
  print("Google Speech Recognition thinks you said " +
        r.recognize_google(audio))
except sr.UnknownValueError:
  print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
  print(
      "Could not request results from Google Speech Recognition service; {0}".
      format(e))

# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import os
openAIkey = os.environ['OPEN_AI']
openai.api_key = openAIkey
audio_file= open("Video_test_1.wav", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript)


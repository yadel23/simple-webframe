import speech_recognition as sr
from os import path

ex = 'Have_A_Dream.wav'

def printWAV(file_name, pos, clip):
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "static/"+file_name)
    text = ''

    r = sr.Recognizer()

    with sr.AudioFile(AUDIO_FILE) as source:
      audio = r.record(source, duration=clip, offset=pos)

      try:
          text += r.recognize_google(audio)

      except sr.UnknownValueError:
          text += "Google Speech Recognition could not understand audio\n"

      except sr.RequestError as e:
          text += "Could not request results from Google Speech Recognition service; {0}".format(e)

    return text
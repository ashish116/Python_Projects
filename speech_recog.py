import speech_recognition as sr
audio_file=("sample.wav")

r = sr.Recognizer()

with sr.AudioFile(audio_file) as source:
    audio = r.record(source)

try:
    print("audio file contains" + r.recognize_google(audio))

except sr.UnknownValueError :
    print("google api is unable to understand audio")
except sr.RequestError :
    print("unable to get result from google API")

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak...")
    audio = r.listen(source)

try:
    print(r.recognize_google(audio))
except:
    print("Could not understand")
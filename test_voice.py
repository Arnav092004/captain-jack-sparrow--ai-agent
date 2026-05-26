import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 165)

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

engine.say("Captain Jack Sparrow online, captain.")

engine.runAndWait()
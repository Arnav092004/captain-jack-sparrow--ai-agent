import pyttsx3
import speech_recognition as sr


class VoiceEngine:

    def __init__(self):

        # SPEAK ENGINE
        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", 170)

        voices = self.engine.getProperty("voices")

        self.engine.setProperty(
            "voice",
            voices[0].id
        )

        # RECOGNIZER
        self.recognizer = sr.Recognizer()

        self.recognizer.energy_threshold = 300

        self.recognizer.dynamic_energy_threshold = True

        self.recognizer.pause_threshold = 0.8

    # =========================
    # SPEAK
    # =========================

    def speak(self, text):

        print(f"AI: {text}")

        self.engine.say(text)

        self.engine.runAndWait()

    # =========================
    # LISTEN
    # =========================

    def listen(self):

        with sr.Microphone() as source:

            print("Listening...")

            # REDUCE NOISE
            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            audio = self.recognizer.listen(
                source,
                phrase_time_limit=5
            )

        try:

            command = self.recognizer.recognize_google(
                audio
            ).lower()

            print(f"You said: {command}")

            return command

        except sr.UnknownValueError:

            return ""

        except sr.RequestError:

            return ""
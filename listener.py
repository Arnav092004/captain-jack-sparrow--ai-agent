import speech_recognition as sr
import threading


class VoiceListener:

    def __init__(self, callback):

        self.recognizer = sr.Recognizer()

        self.microphone = sr.Microphone()

        self.callback = callback

        self.running = False

        self.wake_words = [
            "captain",
            "jack sparrow",
            "captain jack sparrow"
        ]

    def start(self):

        self.running = True

        thread = threading.Thread(target=self.listen_loop)

        thread.daemon = True

        thread.start()

    def stop(self):

        self.running = False

    def listen_loop(self):

        with self.microphone as source:

            self.recognizer.adjust_for_ambient_noise(source)

            print("Voice listener started...")

            while self.running:

                try:

                    audio = self.recognizer.listen(
                        source,
                        timeout=1,
                        phrase_time_limit=5
                    )

                    text = self.recognizer.recognize_google(audio)

                    text = text.lower()

                    print("Heard:", text)

                    for wake_word in self.wake_words:

                        if wake_word in text:

                            command = text.replace(wake_word, "").strip()

                            if command:

                                self.callback(command)

                            break

                except sr.WaitTimeoutError:
                    pass

                except sr.UnknownValueError:
                    pass

                except Exception as e:
                    print("Voice Error:", e)
import tkinter as tk
import math
import threading
import speech_recognition as sr

from voice_engine import VoiceEngine
from system_control import SystemController


class JackSparrowAI:

    def __init__(self):

        # MAIN WINDOW
        self.root = tk.Tk()

        self.root.title("Captain Jack Sparrow")

        self.root.geometry("900x850")

        self.root.configure(bg="#020617")

        self.root.resizable(False, False)

        # SYSTEMS
        self.voice = VoiceEngine()

        self.system = SystemController()

        # ORB
        self.angle = 0

        self.orb_size = 110

        # STATUS
        self.status_text = "IDLE"

        # UI
        self.setup_ui()

        self.animate_orb()

        self.startup_sequence()

        # START VOICE LISTENER
        threading.Thread(
            target=self.start_voice_listener,
            daemon=True
        ).start()

        self.root.mainloop()

    # ====================================
    # UI
    # ====================================
    def setup_ui(self):

        # TITLE
        self.title_label = tk.Label(
            self.root,
            text="CAPTAIN JACK SPARROW",
            font=("Segoe UI", 34, "bold"),
            fg="cyan",
            bg="#020617"
        )

        self.title_label.pack(pady=20)

        # ORB CANVAS
        self.canvas = tk.Canvas(
            self.root,
            width=400,
            height=260,
            bg="#020617",
            highlightthickness=0
        )

        self.canvas.pack()

        # STATUS LABEL
        self.status_label = tk.Label(
            self.root,
            text=self.status_text,
            font=("Segoe UI", 20, "bold"),
            fg="white",
            bg="#020617"
        )

        self.status_label.pack(pady=10)

        # SYSTEM LOG TITLE
        self.logs_label = tk.Label(
            self.root,
            text="SYSTEM LOGS",
            font=("Segoe UI", 18, "bold"),
            fg="cyan",
            bg="#020617"
        )

        self.logs_label.pack(pady=5)

        # CONSOLE
        self.console = tk.Text(
            self.root,
            height=6,
            width=90,
            bg="#081028",
            fg="white",
            insertbackground="white",
            font=("Consolas", 14)
        )

        self.console.pack(pady=10, fill=tk.NONE)

        # COMMAND FRAME
        self.command_frame = tk.Frame(
       self.root,
    bg="#020617"
)

        self.command_frame.pack(
    side=tk.BOTTOM,
    pady=20
)

        # INPUT BOX
        self.command_entry = tk.Entry(
            self.command_frame,
            width=50,
            font=("Segoe UI", 14),
            bg="#081028",
            fg="white",
            insertbackground="white"
        )

        self.command_entry.pack(
            side=tk.LEFT,
            padx=10
        )

        self.command_entry.bind(
            "<Return>",
            lambda event: self.process_command()
        )

        # EXECUTE BUTTON
        self.execute_button = tk.Button(
            self.command_frame,
            text="EXECUTE",
            command=lambda: self.process_command(),
            bg="cyan",
            fg="black",
            font=("Segoe UI", 14, "bold"),
            width=12
        )

        self.execute_button.pack(side=tk.LEFT)
        self.command_frame.lift()

    # ====================================
    # ORB
    # ====================================
    def draw_orb(self):

        self.canvas.delete("all")

        center_x = 200
        center_y = 130

        pulse = math.sin(self.angle) * 8

        size = self.orb_size + pulse

        # OUTER GLOW
        self.canvas.create_oval(
            center_x - size,
            center_y - size,
            center_x + size,
            center_y + size,
            fill="#00F5FF",
            outline=""
        )

        # INNER ORB
        self.canvas.create_oval(
            center_x - size + 20,
            center_y - size + 20,
            center_x + size - 20,
            center_y + size - 20,
            fill="#3465eb",
            outline=""
        )

    def animate_orb(self):

        self.angle += 0.08

        self.draw_orb()

        self.root.after(
            30,
            self.animate_orb
        )

    # ====================================
    # STARTUP
    # ====================================
    def startup_sequence(self):

        self.log("Captain Jack Sparrow online.")

        self.log("Voice listener started.")

        self.voice.speak(
            "Captain Jack Sparrow online captain."
        )

    # ====================================
    # LOGGING
    # ====================================
    def log(self, text):

        self.console.insert(
            tk.END,
            f"{text}\n"
        )

        self.console.see(tk.END)

    # ====================================
    # COMMAND PROCESSING
    # ====================================
    def process_command(self, command=None):

        if command is None:

            command = self.command_entry.get().lower()

        else:

            command = command.lower()

        if not command.strip():

            return

        self.log(f"> {command}")

        self.command_entry.delete(0, tk.END)

        response = "Command not recognized."

        # REMOVE WAKE WORDS
        wake_words = [
            "captain",
            "jack",
            "captain jack sparrow"
        ]

        for wake in wake_words:

            if command.startswith(wake):

                command = command.replace(wake, "").strip()

        # ========================
        # OPEN
        # ========================
        if command.startswith("open"):

            item = command.replace(
                "open",
                ""
            ).strip()

            websites = [

                "youtube",
                "instagram",
                "whatsapp",
                "google",
                "github",
                "facebook",
                "gmail",
                "chatgpt"

            ]

            if item in websites:

                response = self.system.open_website(item)

            else:

                response = self.system.open_app(item)

        # ========================
        # CLOSE
        # ========================
        elif command.startswith("close"):

            app = command.replace(
                "close",
                ""
            ).strip()

            response = self.system.close_app(app)

        # ========================
        # SCREENSHOT
        # ========================
        elif "screenshot" in command:

            response = self.system.take_screenshot()

        # ========================
        # VOLUME
        # ========================
        elif "volume up" in command:

            response = self.system.volume_up()

        elif "volume down" in command:

            response = self.system.volume_down()

        elif "mute" in command:

            response = self.system.mute_volume()

        # ========================
        # SYSTEM
        # ========================
        elif "shutdown" in command:

            response = self.system.shutdown_pc()

        elif "restart" in command:

            response = self.system.restart_pc()

        elif "lock" in command:

            response = self.system.lock_pc()

        # RESPONSE
        self.log(response)

        self.voice.speak(response)

    # ====================================
    # VOICE LISTENER
    # ====================================
    def start_voice_listener(self):

        recognizer = sr.Recognizer()

        microphone = sr.Microphone()

        while True:

            try:

                with microphone as source:

                    recognizer.adjust_for_ambient_noise(
                        source,
                        duration=0.5
                    )

                    print("Listening...")

                    audio = recognizer.listen(
                        source
                    )

                command = recognizer.recognize_google(
                    audio
                ).lower()

                print("USER:", command)

                # WAKE WORDS
                wake_words = [

                    "captain",
                    "jack",
                    "captain jack sparrow"

                ]

                for wake in wake_words:

                    if wake in command:

                        cleaned = command.replace(
                            wake,
                            ""
                        ).strip()

                        self.log(
                            f"[VOICE] {command}"
                        )

                        self.process_command(
                            cleaned
                        )

                        break

            except:

                pass


if __name__ == "__main__":

    JackSparrowAI()
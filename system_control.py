import os
import subprocess
import webbrowser
import pyautogui


class SystemController:

    # =========================
    # OPEN APPLICATIONS
    # =========================
    def open_app(self, app_name):

        app_name = app_name.lower()

        apps = {

            "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",

            "vs code": r"C:\Users\Win11\AppData\Local\Programs\Microsoft VS Code\Code.exe",

            "notepad": "notepad.exe",

            "calculator": "calc.exe",

            "paint": "mspaint.exe",

            "cmd": "cmd.exe",

            "explorer": "explorer.exe"

        }

        try:

            if app_name in apps:

                subprocess.Popen(apps[app_name])

                return f"Opening {app_name}"

            else:

                return f"{app_name} not found."

        except Exception as e:

            return str(e)

    # =========================
    # CLOSE APPLICATIONS
    # =========================
    def close_app(self, app_name):

        processes = {

            "chrome": "chrome.exe",

            "vs code": "Code.exe",

            "notepad": "notepad.exe",

            "calculator": "CalculatorApp.exe"

        }

        try:

            if app_name in processes:

                os.system(
                    f'taskkill /f /im "{processes[app_name]}"'
                )

                return f"Closed {app_name}"

            else:

                return f"{app_name} not found."

        except Exception as e:

            return str(e)

    # =========================
    # WEBSITES
    # =========================
    def open_website(self, site):

        websites = {

            "youtube": "https://www.youtube.com",

            "instagram": "https://www.instagram.com",

            "whatsapp": "https://web.whatsapp.com",

            "google": "https://www.google.com",

            "github": "https://github.com",

            "facebook": "https://facebook.com",

            "gmail": "https://mail.google.com",

            "chatgpt": "https://chat.openai.com"

        }

        site = site.lower().strip()

        try:

            if site in websites:

                webbrowser.open(websites[site])

                return f"Opening {site}"

            else:

                return f"{site} not found."

        except Exception as e:

            return str(e)

    # =========================
    # SCREENSHOT
    # =========================
    def take_screenshot(self):

        try:

            screenshot = pyautogui.screenshot()

            screenshot.save("screenshot.png")

            return "Screenshot saved."

        except Exception as e:

            return str(e)

    # =========================
    # VOLUME
    # =========================
    def volume_up(self):

        pyautogui.press("volumeup")

        return "Volume increased."

    def volume_down(self):

        pyautogui.press("volumedown")

        return "Volume decreased."

    def mute_volume(self):

        pyautogui.press("volumemute")

        return "Volume muted."

    # =========================
    # SYSTEM CONTROLS
    # =========================
    def shutdown_pc(self):

        os.system("shutdown /s /t 5")

        return "Shutting down PC."

    def restart_pc(self):

        os.system("shutdown /r /t 5")

        return "Restarting PC."

    def lock_pc(self):

        os.system("rundll32.exe user32.dll,LockWorkStation")

        return "Locking PC."
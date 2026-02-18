import subprocess
import threading

import rumps

# Ping Target
TARGET = "8.8.8.8"
# Ping Interval
INTERVAL = 5

class PingApp(rumps.App):
    def __init__(self):
        super().__init__("🔴")
        self.menu = [
            rumps.MenuItem(f"Pinging: {TARGET}"),
            None,
            rumps.MenuItem("Exit", callback=rumps.quit_application)
        ]
        self.check_loop()

    def ping(self):
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "2000", TARGET],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0

    def check_loop(self):
        def loop():
            while True:
                ok = self.ping()
                self.title = "🟢" if ok else "🔴"
                threading.Event().wait(INTERVAL)
        t = threading.Thread(target=loop, daemon=True)
        t.start()

if __name__ == "__main__":
    PingApp().run()

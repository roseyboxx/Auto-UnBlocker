import rumps
import subprocess
from pathlib import Path

SCRIPT_PATH = Path.home() / "ub/ub.py"

class Widget(rumps.App):
    def __init__(self):
        super().__init__(name="◉", title="◉")
        self.menu = ["Open"]

    @rumps.clicked("Open")
    def run_script(self, _):
        subprocess.Popen(["/usr/local/bin/python3", str(SCRIPT_PATH)])

if __name__ == "__main__":
    Widget().run()


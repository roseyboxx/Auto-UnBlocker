import os
import sys
import urllib.request
import subprocess
from pathlib import Path
import ssl

BASE_URL = "https://download-prx.izziefinnegan.workers.dev/?url=https://github.com/roseyboxx/Auto-UnBlocker/releases/latest/download/"  # you host these
MAIN_SCRIPT = "ub.py"
WIDGET_SCRIPT = "widget.py"

INSTALL_DIR = Path.home() / "ub"
LAUNCH_AGENT_PATH = Path.home() / "Library/LaunchAgents/com.example.ub.plist"

def prompt():
    print("""
Continue? (y/N)
""")
    return input("> ").strip().lower() == "y"

def download(name):
    url = f"{BASE_URL}/{name}"
    dest = INSTALL_DIR / name
    print(f"Downloading {url}")

    # Create an SSL context that ignores certificate verification
    context = ssl._create_unverified_context()

    opener = urllib.request.build_opener(
        urllib.request.HTTPSHandler(context=context)
    )
    urllib.request.install_opener(opener)

    urllib.request.urlretrieve(url, dest)


def create_launch_agent():
    INSTALL_DIR.mkdir(exist_ok=True)

    plist = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
 "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.example.ub</string>

    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/python3</string>
        <string>{INSTALL_DIR / WIDGET_SCRIPT}</string>
    </array>

    <key>RunAtLoad</key>
    <true/>

    <key>KeepAlive</key>
    <false/>

    <key>StandardOutPath</key>
    <string>{INSTALL_DIR}/out.log</string>

    <key>StandardErrorPath</key>
    <string>{INSTALL_DIR}/err.log</string>
</dict>
</plist>
"""

    LAUNCH_AGENT_PATH.write_text(plist)

    # IMPORTANT: unload first if it exists
    subprocess.run(
        ["launchctl", "bootout", f"gui/{os.getuid()}", str(LAUNCH_AGENT_PATH)],
        stderr=subprocess.DEVNULL
    )

    subprocess.run(
        ["launchctl", "bootstrap", f"gui/{os.getuid()}", str(LAUNCH_AGENT_PATH)],
        check=True
    )



def main():
    if not prompt():
        print("Installation cancelled.")
        sys.exit(0)

    INSTALL_DIR.mkdir(exist_ok=True)

    download(MAIN_SCRIPT)
    download(WIDGET_SCRIPT)

    create_launch_agent()

    subprocess.run("/usr/local/bin/python3 -m pip install rumps".split())
    subprocess.run("/usr/local/bin/python3 -m pip install urllib3".split())
    print("Installation complete.")
    print("The ◉ widget will appear in the menu bar.")

if __name__ == "__main__":
    main()


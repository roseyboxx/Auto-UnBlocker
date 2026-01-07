import tkinter as tk
import subprocess
import sys
from pathlib import Path
import os

# Full path to the script file
script_path = Path(__file__).resolve()
print("Script path:", script_path)

# Folder containing the script
script_folder = script_path.parent

# urllib3

try:
    import requests
    print("requests module already installed and imported successfully.")
except ImportError:
    print("requests module not found. Attempting to install...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        import requests
        print("requests module installed and imported successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Installation failed: {e}")
        print("Please try running 'pip install requests' from your terminal manually.")
    except ImportError:
        print("Installation succeeded, but importing still failed. There might be an environment issue.")

try:
    import urllib3
    print("urllib3 module already installed and imported successfully.")
except ImportError:
    print("urllib3 module not found. Attempting to install...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "urllib3"])
        import urllib3
        print("requests module installed and imported successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Installation failed: {e}")
        print("Please try running 'pip install urllib3' from your terminal manually.")
    except ImportError:
        print("Installation succeeded, but importing still failed. There might be an environment issue.")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

filename = str(script_folder / "MC.py")
mcpy = "https://download-prx.izziefinnegan.workers.dev/?url=https://github.com/roseyboxx/School-MCLauncher/releases/latest/download/launcher.py"

chrome = "open -a 'Google Chrome.app' --args --proxy-server='socks5://73.203.240.183:8000'"

def on_chrome_click():
    subprocess.run(["killall", "Google Chrome"])
    subprocess.run([
        "open", "-a", "Google Chrome.app",
        "--args", "--proxy-server=socks5://73.203.240.183:8000"
    ])


def on_mc_click():
    if Path(filename).exists():
        print(f"File '{filename}' exists. Running it...")
        subprocess.run([sys.executable, filename])
    else:
        print(f"Error: The file '{filename}' was not found, downloading...")
        try:
            # Ignore SSL certificate verification
            response = requests.get(mcpy, verify=False)

            if response.status_code == 200:
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f"File '{filename}' downloaded successfully! Opening")
                subprocess.run([sys.executable, filename])
            else:
                print(f"Failed to download file. Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"An error occurred while downloading: {e}")
            
root = tk.Tk()
root.title("De-Restricor")
root.geometry("300x150")

chrome_button = tk.Button(root, text="Unblock Chrome", command=on_chrome_click)
chrome_button.pack(pady=5)

mc_button = tk.Button(root, text="Open MC Launcher", command=on_mc_click)
mc_button.pack(pady=5)

root.mainloop()

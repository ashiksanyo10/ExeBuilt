import os
import threading
import time
from tkinter import Tk, Label
from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

LOADING_MESSAGES = [
    "Baking cookies...",
    "Warming up the servers...",
    "Feeding the hamsters...",
    "Polishing the screen...",
    "Counting stars...",
    "Scrapper Engine Running"
]

def show_splash():
    # Initialize Tkinter splash window
    splash = Tk()
    splash.title("Loading...")
    splash.geometry("300x100")  # 3 cm height, 10 cm width
    splash.configure(bg="#f0f0f0")  # Light gray background
    splash.overrideredirect(True)  # Remove title bar
    splash.eval('tk::PlaceWindow . center')  # Center the window

    label = Label(splash, text="", font=("Arial", 12), bg="#f0f0f0")
    label.pack(expand=True)

    # Cycle through loading messages
    for message in LOADING_MESSAGES:
        label.config(text=message)
        splash.update()
        time.sleep(1.5)

    splash.destroy()  # Close the splash screen
    time.sleep(0.5)

def start_flask():
    app.run(port=8080, debug=False, use_reloader=False)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()  # For PyInstaller compatibility

    # Show splash screen
    show_splash()

    # Start Flask server in a separate thread
    threading.Thread(target=start_flask, daemon=True).start()

    # Keep script running to serve Flask
    while True:
        time.sleep(1)


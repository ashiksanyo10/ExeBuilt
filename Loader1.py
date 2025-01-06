from tkinter import Tk, Label
import threading
import time
from flask import Flask, render_template
import webview

# Flask app setup
app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/')
def index():
    return render_template('index.html')

# Loading messages for splash screen
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

    label = Label(splash, text="", font=("Arial", 12), bg="#f0f0f0")
    label.pack(expand=True)

    # Cycle through loading messages
    for message in LOADING_MESSAGES:
        label.config(text=message)
        splash.update()
        time.sleep(1.5)

    splash.destroy()  # Close the splash screen
    time.sleep(0.5)  # Ensure smooth transition before launching the app

def start_flask():
    app.run(port=8080, debug=False, use_reloader=False)

if __name__ == "__main__":
    # Run the splash screen before starting the app
    show_splash()

    # Start Flask in a separate thread
    threading.Thread(target=start_flask).start()

    # Start PyWebView
    webview.create_window("Movie Scraper Tool", "http://127.0.0.1:8080")
    webview.start()

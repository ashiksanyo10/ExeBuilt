import os
import threading
import time
from flask import Flask, render_template, request, jsonify, send_from_directory
import webview
from tkinter import Tk, Label

# Flask app setup
app = Flask(__name__, template_folder="templates", static_folder="static")

# Sarcastic loading messages
LOADING_MESSAGES = [
    "Baking cookies...",
    "Warming up the servers...",
    "Feeding the hamsters...",
    "Polishing the screen...",
    "Counting stars...",
    "Scrapper Engine Running"
]

# Splash screen setup
def show_splash():
    splash = Tk()
    splash.title("Loading...")
    splash.geometry("300x100")  # 3 cm height, 10 cm width
    splash.configure(bg="#f0f0f0")  # Light gray background
    splash.overrideredirect(True)  # Remove title bar

    label = Label(splash, text="", font=("Arial", 12), bg="#f0f0f0")
    label.pack(expand=True)

    # Display loading messages
    for message in LOADING_MESSAGES:
        label.config(text=message)
        splash.update()
        time.sleep(1.5)  # Wait 1.5 seconds before changing message

    splash.destroy()  # Close the splash screen

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Your upload logic here...
    pass

@app.route('/download/<filename>')
def download_file(filename):
    # Your download logic here...
    pass

def start_flask():
    print("Starting Flask server...")
    app.run(port=8080, debug=False, use_reloader=False)

if __name__ == "__main__":
    # Create uploads folder if it doesn't exist
    os.makedirs("uploads", exist_ok=True)

    # Start the splash screen in the main thread
    show_splash()

    # Start Flask server in a separate thread
    threading.Thread(target=start_flask).start()

    # Start PyWebView after the splash screen
    webview.create_window("Movie Scraper Tool", "http://127.0.0.1:8080")
    webview.start()

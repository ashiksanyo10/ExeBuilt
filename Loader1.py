import os
import threading
import time
from tkinter import Tk, Label
from flask import Flask, render_template, request, jsonify, send_from_directory
import webview

# Flask app setup
app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/')
def index():
    return render_template('index.html')

# Loading messages for the splash screen
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
    splash.geometry("300x100")  # Set size (3 cm x 10 cm)
    splash.configure(bg="#f0f0f0")  # Light gray background
    splash.overrideredirect(True)  # Remove the title bar

    # Center the splash screen on the screen
    screen_width = splash.winfo_screenwidth()
    screen_height = splash.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (300 / 2))
    y_cordinate = int((screen_height / 2) - (100 / 2))
    splash.geometry(f"300x100+{x_cordinate}+{y_cordinate}")

    # Add a label with Rubik font
    try:
        splash.option_add("*Font", "Rubik 12")
    except:
        pass

    label = Label(splash, text="", font=("Rubik", 12), bg="#f0f0f0")
    label.pack(expand=True)

    # Cycle through loading messages
    for message in LOADING_MESSAGES:
        label.config(text=message)
        splash.update()
        time.sleep(1.5)  # Wait 1.5 seconds before changing the message

    splash.destroy()  # Close the splash screen
    time.sleep(0.5)  # Ensure smooth transition

def start_flask():
    print("Starting Flask server...")
    app.run(port=8080, debug=False, use_reloader=False)

if __name__ == "__main__":
    # Create uploads folder if it doesn't exist
    os.makedirs("uploads", exist_ok=True)

    # Run the splash screen before starting the app
    show_splash()

    # Start Flask in a separate thread
    threading.Thread(target=start_flask).start()

    # Start PyWebView after the splash screen
    webview.create_window("Movie Scraper Tool", "http://127.0.0.1:8080")
    webview.start()

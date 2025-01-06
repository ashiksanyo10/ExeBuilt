from tkinter import Tk, Label, Canvas
import threading
import time
from flask import Flask, render_template
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
    splash.geometry("400x200")  # Larger window for visual design
    splash.configure(bg="#f0f0f0")  # Fallback background
    splash.overrideredirect(True)  # Remove the title bar

    # Center the splash screen on the screen
    screen_width = splash.winfo_screenwidth()
    screen_height = splash.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (400 / 2))
    y_cordinate = int((screen_height / 2) - (200 / 2))
    splash.geometry(f"400x200+{x_cordinate}+{y_cordinate}")

    # Create a gradient background
    canvas = Canvas(splash, width=400, height=200)
    canvas.pack(fill="both", expand=True)

    for i in range(200):
        color = f"#{hex(240 - i)[2:].zfill(2)}{hex(240 - i)[2:].zfill(2)}FF"
        canvas.create_rectangle(0, i, 400, i + 1, outline=color, fill=color)

    # Add a label for loading messages
    label = Label(splash, text="", font=("Rubik", 14, "bold"), bg="#0000FF", fg="white")
    label.place(relx=0.5, rely=0.5, anchor="center")  # Center the label

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
    # Show splash screen before starting the app
    show_splash()

    # Start Flask in a separate thread
    threading.Thread(target=start_flask).start()

    # Start PyWebView
    webview.create_window("Movie Scraper Tool", "http://127.0.0.1:8080")
    webview.start()

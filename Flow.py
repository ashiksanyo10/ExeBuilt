import os
import threading
import time
import keyboard
from flask import Flask, request, jsonify, send_from_directory, render_template
from tkinter import Tk, Label
import pandas as pd
import logging

app = Flask(__name__, template_folder="templates")
logging.basicConfig(level=logging.DEBUG)

LOADING_MESSAGES = [
    "Warming up the servers 🔥",
    "Baking cookies 🍪",
    "Feeding the hamsters 🐰",
    "Polishing the screen 📺",
    "Counting stars ⭐",
    "Scrapper Engine Running ✅",
    "Server active on Chrome ⚡"
]

# Directory to store output files
UPLOAD_DIR = os.path.join(os.getcwd(), 'uploads')
os.makedirs(UPLOAD_DIR, exist_ok=True)

def show_splash():
    """Display a splash screen with loading messages."""
    splash = Tk()
    splash.title("Loading...")
    splash.geometry("300x100")
    splash.configure(bg="#f0f0f0")
    splash.overrideredirect(True)
    splash.eval('tk::PlaceWindow . center')  # Center the window

    label = Label(splash, text="", font=("Helvetica", 12), bg="#f0f0f0")
    label.pack(expand=True)

    for message in LOADING_MESSAGES:
        label.config(text=message)
        splash.update()
        time.sleep(1.5)

    splash.destroy()

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and scraping logic."""
    try:
        file = request.files['file']
        if not file.filename.endswith('.xlsx'):
            return jsonify({'error': 'Invalid file format. Please upload an Excel file.'})

        # Save the uploaded file
        timestamp = int(time.time())
        input_filename = f"{os.path.splitext(file.filename)[0]}_{timestamp}.xlsx"
        input_file_path = os.path.join(UPLOAD_DIR, input_filename)
        file.save(input_file_path)

        # Process the uploaded file
        df = pd.read_excel(input_file_path)
        df['Processed'] = "Simulated Data"  # Placeholder for your scraping logic

        # Save processed data
        output_filename = f"movie_ratings_{timestamp}.xlsx"
        output_file_path = os.path.join(UPLOAD_DIR, output_filename)
        df.to_excel(output_file_path, index=False)

        return jsonify({'download_url': f'/download/{output_filename}'})
    except Exception as e:
        logging.error(f"Error processing upload: {e}")
        return jsonify({'error': 'An error occurred while processing the file.'})

@app.route('/download/<filename>')
def download_file(filename):
    """Allow users to download processed files."""
    file_path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found!'}), 404
    return send_from_directory(UPLOAD_DIR, filename, as_attachment=True)

def start_flask():
    """Start the Flask server."""
    app.run(port=8080, debug=False, use_reloader=False)

def listen_to_quit():
    """Listen for Ctrl+Q to quit the application."""
    print("Press Ctrl+Q to quit the application.")
    keyboard.add_hotkey('ctrl+q', lambda: os._exit(0))

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()  # Ensure compatibility with PyInstaller

    # Start the Flask server in a separate thread
    flask_thread = threading.Thread(target=start_flask, daemon=True)
    flask_thread.start()

    # Start the keyboard listener in a separate thread
    keyboard_thread = threading.Thread(target=listen_to_quit, daemon=True)
    keyboard_thread.start()

    # Show the splash screen
    show_splash()

    # Keep the application running
    while True:
        time.sleep(1)

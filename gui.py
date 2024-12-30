import tkinter as tk
from tkinter import messagebox
import threading
import scraper

def start_scraping():
    threading.Thread(target=scraper.scrape_gti).start()

def stop_scraping():
    scraper.stop_scraper()
    messagebox.showinfo("Info", "Scraper stopped!")

# Tkinter GUI
root = tk.Tk()
root.title("GTI Review Application")

start_button = tk.Button(root, text="Start", command=start_scraping, width=15)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop", command=stop_scraping, width=15)
stop_button.pack(pady=10)

root.mainloop()

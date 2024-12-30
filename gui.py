import tkinter as tk
from tkinter import messagebox
import threading
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Flask API URL
API_URL = 'http://127.0.0.1:5000/check_duplicate'

# Selenium WebDriver Setup
driver = webdriver.Chrome(executable_path='path_to_chromedriver')

# Function to scrape and check GTIs
def scrape_and_notify():
    try:
        driver.get('https://www.md.dev/')
        time.sleep(3)  # Adjust based on page load time

        # Example selectors for GTI and Task ID elements
        gti_elements = driver.find_elements(By.CLASS_NAME, 'gti-class')
        task_id_elements = driver.find_elements(By.CLASS_NAME, 'task-id-class')

        for gti, task_id in zip(gti_elements, task_id_elements):
            payload = {
                'gti': gti.text,
                'task_id': task_id.text
            }
            response = requests.post(API_URL, json=payload)
            result = response.json()

            # Show popup based on the response
            if result['status'] == 'duplicate':
                messagebox.showwarning("Duplicate Detected", f"GTI: {gti.text}\nOld Task ID: {result.get('old_task_id')}\nNew Task ID: {task_id.text}")
            elif result['status'] == 'success':
                messagebox.showinfo("New GTI Added", f"GTI: {gti.text}\nTask ID: {task_id.text}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to stop the scraper
def stop_scraper():
    driver.quit()
    messagebox.showinfo("Info", "Scraper stopped!")

# GUI with Tkinter
def start_gui():
    root = tk.Tk()
    root.title("GTI Review Application")

    start_button = tk.Button(root, text="Start", command=lambda: threading.Thread(target=scrape_and_notify).start(), width=15)
    start_button.pack(pady=10)

    stop_button = tk.Button(root, text="Stop", command=stop_scraper, width=15)
    stop_button.pack(pady=10)

    root.mainloop()

# Start the GUI
if __name__ == "__main__":
    start_gui()

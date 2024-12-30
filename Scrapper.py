from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

# Flask API URL
API_URL = 'http://127.0.0.1:5000/check_duplicate'

# Selenium WebDriver Setup
driver = webdriver.Chrome(executable_path='path_to_chromedriver')

def scrape_gti():
    driver.get('https://www.md.dev/')
    time.sleep(3)  # Adjust based on page load time

    # Example selectors
    gti_elements = driver.find_elements(By.CLASS_NAME, 'gti-class')
    task_id_elements = driver.find_elements(By.CLASS_NAME, 'task-id-class')

    for gti, task_id in zip(gti_elements, task_id_elements):
        payload = {
            'gti': gti.text,
            'task_id': task_id.text
        }
        response = requests.post(API_URL, json=payload)
        print(response.json())

# Close the driver
def stop_scraper():
    driver.quit()

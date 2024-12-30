from helium import start_chrome, find_all, kill_browser
import time

def test_scraper():
    try:
        # Start Chrome browser
        browser = start_chrome('https://www.md.dev/', headless=False)  # Change URL if needed
        time.sleep(3)  # Adjust for page load time

        # Example selectors for GTI and Task ID (replace with actual ones)
        gti_elements = find_all('.gti-class')  # Replace with actual GTI class
        task_id_elements = find_all('.task-id-class')  # Replace with actual Task ID class

        for gti, task_id in zip(gti_elements, task_id_elements):
            print(f"GTI: {gti.web_element.text}, Task ID: {task_id.web_element.text}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        kill_browser()

if __name__ == "__main__":
    test_scraper()

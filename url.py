def wait_for_flask():
    """Wait for Flask to start before proceeding."""
    url = "http://127.0.0.1:8080"
    for _ in range(20):  # Wait up to 10 seconds
        try:
            import requests
            response = requests.get(url)
            if response.status_code == 200:
                print("Flask server is ready.")
                return True
        except:
            time.sleep(0.5)  # Retry every 0.5 seconds
    print("Flask server did not start in time.")
    return False

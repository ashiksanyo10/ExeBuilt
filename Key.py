def listen_for_exit():
    """Listen for keyboard shortcut to quit the application."""
    print("Press Ctrl+Q to quit the application.")
    keyboard.add_hotkey('ctrl+q', lambda: os._exit(0))  # Terminate the app

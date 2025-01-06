def create_tray_icon():
    # Load the application icon
    icon_path = os.path.join(os.getcwd(), 'app_icon.ico')
    icon_image = Image.open(icon_path)

    # Define the system tray menu
    menu = Menu(MenuItem('Quit', quit_application))

    # Create the tray icon
    icon = Icon("Scraper Tool", icon_image, menu=menu)
    icon.run()

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()

    # Start the system tray icon in a separate thread
    threading.Thread(target=create_tray_icon, daemon=True).start()

    # Show splash screen
    show_splash()

    # Start Flask server in a separate thread
    flask_thread = threading.Thread(target=start_flask, daemon=True)
    flask_thread.start()

    # Wait for the exit event
    try:
        exit_event.wait()
    except KeyboardInterrupt:
        print("Application interrupted. Exiting...")
        os._exit(0)

def show_splash():
    # Initialize Tkinter splash window
    splash = Tk()
    splash.title("Loading...")
    splash.geometry("300x100")  # 3 cm height, 10 cm width
    splash.configure(bg="#f0f0f0")  # Light gray background
    splash.overrideredirect(True)  # Remove title bar
    splash.eval('tk::PlaceWindow . center')  # Center the window

    label = Label(splash, text="", font=("Arial", 12), bg="#f0f0f0")
    label.pack(expand=True)

    # Cycle through loading messages
    for message in LOADING_MESSAGES:
        label.config(text=message)
        splash.update()
        time.sleep(1.5)

    splash.destroy()  # Close the splash screen
    time.sleep(0.5) 

if __name__ == "__main__":
    # Run the splash screen before starting the app
    show_splash()

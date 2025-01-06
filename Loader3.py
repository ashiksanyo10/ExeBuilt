def show_loading_window():
    root = Tk()
    root.title("Starting Scraper...")
    root.geometry("300x100")
    root.eval('tk::PlaceWindow . center')  # Center the window

    label = Label(root, text="", font=("Helvetica", 12))
    label.pack(expand=True)

    def update_message(index=0):
        if index < len(LOADING_MESSAGES):
            label.config(text=LOADING_MESSAGES[index])
            root.after(1000, update_message, index + 1)
        else:
            root.destroy()

    update_message()
    root.mainloop()

if __name__ == '__main__':
    # Ensure uploads directory exists
    os.makedirs("uploads", exist_ok=True)

    # Start Flask server in a thread
    threading.Thread(target=start_flask, daemon=True).start()

    # Show loading window
    show_loading_window()

    # Keep the script running
    while True:
        time.sleep(1)

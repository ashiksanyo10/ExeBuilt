import tkinter as tk

def test_gui():
    root = tk.Tk()
    root.title("GTI Review Application")

    start_button = tk.Button(root, text="Start", width=15)
    start_button.pack(pady=10)

    stop_button = tk.Button(root, text="Stop", width=15)
    stop_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    test_gui()

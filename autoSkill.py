import tkinter as tk
from tkinter import messagebox
import pyautogui
import threading
import time

class AutoKeyPresser(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Auto Key Presser")
        self.geometry("300x500")

        self.key_to_press = [tk.StringVar(self) for _ in range(5)]
        self.frequency = [tk.DoubleVar(self) for _ in range(5)]
        self.threads = []

        for i in range(5):
            tk.Label(self, text=f"Key to Press {i+1}:").pack()
            tk.Entry(self, textvariable=self.key_to_press[i]).pack()
            tk.Label(self, text=f"Frequency {i+1} (seconds):").pack()
            tk.Entry(self, textvariable=self.frequency[i]).pack()

        tk.Button(self, text="Start", command=self.start).pack()
        tk.Button(self, text="Stop", command=self.stop).pack()

        # Copyright Label
        frame = tk.Frame(self)
        frame.pack(side="bottom", fill="x", pady=10)
        tk.Label(frame, text="\u00A9 2023 PeachBlack").pack()

        self.should_press = threading.Event()

    def start(self):
        self.start_pressing()
        messagebox.showinfo("Started", "Key pressing has started.")

    def start_pressing(self):
        self.should_press.set()
        for i in range(5):
            t = threading.Thread(target=self.press_key, args=(i,))
            t.start()
            self.threads.append(t)

    def press_key(self, index):
        while self.should_press.is_set():
            pyautogui.press(self.key_to_press[index].get())
            time.sleep(self.frequency[index].get())

    def stop(self):
        threading.Thread(target=self.stop_pressing).start()

    def stop_pressing(self):
        self.should_press.clear()
        for t in self.threads:
            t.join()  # ensure all threads have stopped
        self.threads = []
        messagebox.showinfo("Stopped", "Key pressing has stopped.")

    def close_window(self):
        threading.Thread(target=self.stop_pressing).start()
        self.destroy()

    def run(self):
        self.protocol("WM_DELETE_WINDOW", self.close_window)
        super().mainloop()

if __name__ == "__main__":
    app = AutoKeyPresser()
    app.run()

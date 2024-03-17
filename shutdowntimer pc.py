import os
import time
import threading
import tkinter as tk

class CountdownTimer:
    def __init__(self, master, total_seconds):
        self.master = master
        self.total_seconds = total_seconds
        self.remaining_seconds = total_seconds
        self.label = tk.Label(master, text="", font=("Arial", 18))
        self.label.pack()
        self.update_timer()

    def update_timer(self):
        hours, remainder = divmod(self.remaining_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.label.config(text="Shutdown in: {:02}:{:02}:{:02}".format(hours, minutes, seconds))
        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1
            self.master.after(1000, self.update_timer)
        else:
            os.system("shutdown /s /t 1")
def log_running_status(): # Log the status of the timer to a file every second while it's running
    while True: 
        print("Das Skript läuft noch.")
        time.sleep(30)


def start_shutdown_timer(hours, minutes):
    total_seconds = hours * 3600 + minutes * 60
    time.sleep(total_seconds)
    os.system("shutdown /s /t 1")

def start_timer_from_input():
    global root  # Markiere 'root' als global
    hours = int(hours_entry.get())
    minutes = int(minutes_entry.get())
    total_seconds = hours * 3600 + minutes * 60
    root.destroy()  # Schließe das Eingabefenster
    root = tk.Tk()
    root.title("Shutdown Timer")
    timer = CountdownTimer(root, total_seconds)
    threading.Thread(target=start_shutdown_timer, args=(hours, minutes), daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Shutdown Timer - Eingabe")

    tk.Label(root, text="Stunden:").grid(row=0, column=0)
    tk.Label(root, text="Minuten:").grid(row=1, column=0)

    hours_entry = tk.Entry(root)
    minutes_entry = tk.Entry(root)

    hours_entry.grid(row=0, column=1)
    minutes_entry.grid(row=1, column=1)

    start_button = tk.Button(root, text="Start Timer", command=start_timer_from_input)
    start_button.grid(row=2, columnspan=2)

    root.mainloop()


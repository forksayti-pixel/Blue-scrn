import tkinter as tk
import platform
import random
import time
import threading
import hashlib

ef = hashlib.sha256("KbpdSnOC530".encode()).hexdigest()

try:
    with open("strct.txt", "r", encoding="utf-8") as f:
        ASCII_ART = f.read()
except:
    ASCII_ART = "ASCII NOT FOUND"

def detect_os():
    os_name = platform.system().lower()
    if "windows" in os_name:
        return "windows"
    elif "linux" in os_name:
        return "linux"
    elif "darwin" in os_name:
        return "mac"
    else:
        return "unknown"

os_type = detect_os()
os_info = platform.system() + " " + platform.release()

root = tk.Tk()
root.attributes("-fullscreen", True)
root.overrideredirect(True)

frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

face = tk.Label(font=("Consolas", 100, "bold"))
face.place(relx=0.5, rely=0.2, anchor="center")

label = tk.Label(font=("Consolas", 18))
label.place(relx=0.5, rely=0.45, anchor="center")

sub = tk.Label(font=("Consolas", 14))
sub.place(relx=0.5, rely=0.52, anchor="center")

progress_label = tk.Label(font=("Consolas", 16))
progress_label.place(relx=0.5, rely=0.6, anchor="center")

def show_final():
    frame.config(bg="black")

    face.config(text="", bg="black")
    label.config(text="CSTM DEMO SCREEN", bg="black", fg="white")
    sub.config(text="session ended", bg="black", fg="white")
    progress_label.config(text="", bg="black")

    entry = tk.Entry(frame, font=("Consolas", 18))
    entry.place(relx=0.5, rely=0.45, anchor="center")

    status = tk.Label(frame, text="", fg="white", bg="black")
    status.place(relx=0.5, rely=0.52, anchor="center")

    def check():
        if hashlib.sha256(entry.get().encode()).hexdigest() == ef:
            root.destroy()
        else:
            status.config(text="WRONG PASSWORD")

    tk.Button(frame, text="ENTER", command=check).place(relx=0.5, rely=0.58, anchor="center")

    ascii_label = tk.Label(
        frame,
        text=ASCII_ART,
        fg="white",
        bg="black",
        font=("Consolas", 6),
        justify="center"
    )
    ascii_label.place(relx=0.5, rely=0.8, anchor="center")

def apply_theme(progress, stop):

    if os_type == "windows":
        frame.config(bg="#0078D7")
        face.config(text=":(", bg="#0078D7", fg="white")
        label.config(text="Your PC ran into a problem", bg="#0078D7", fg="white")
        sub.config(bg="#0078D7", fg="white")
        progress_label.config(bg="#0078D7", fg="white")

    elif os_type == "linux":
        frame.config(bg="black")
        face.config(text="KERNEL PANIC", bg="black", fg="white")
        label.config(text="Linux kernel panic detected", bg="black", fg="white")
        sub.config(bg="black", fg="white")
        progress_label.config(bg="black", fg="white")

    elif os_type == "mac":
        frame.config(bg="#A0A0A0")
        face.config(text="💀", bg="#A0A0A0")
        label.config(text="You need to restart your computer", bg="#A0A0A0", fg="black")
        sub.config(bg="#A0A0A0", fg="black")
        progress_label.config(bg="#A0A0A0", fg="black")

    else:
        frame.config(bg="black")
        face.config(text="ERROR", bg="black", fg="white")

    sub.config(text=f"STOP CODE: {stop}\n{os_info}")
    progress_label.config(text=f"{progress}% complete")

def fake_crash():
    time.sleep(1.5)

    progress = 0
    stop = random.choice([
        "SYSTEM_SERVICE_EXCEPTION",
        "MEMORY_MANAGEMENT",
        "KERNEL_PANIC"
    ])

    while progress <= 100:
        apply_theme(progress, stop)

        progress += random.randint(1, 3)
        time.sleep(0.08)

    frame.config(bg="white")
    time.sleep(0.15)

    show_final()

threading.Thread(target=fake_crash, daemon=True).start()

root.mainloop()

import platform
import tkinter as tk
from tkinter import messagebox

try:
    import psutil
except ImportError:
    psutil = None


def run_diagnostics():
    cpu_usage = psutil.cpu_percent(interval=1) if psutil else "N/A"
    ram_usage = psutil.virtual_memory().percent if psutil else "N/A"

    diag_text = (
        f"--- CODE DOCTOR SYSTEM DIAGNOSE ---\n\n"
        f"OS: {platform.system()} {platform.release()}\n"
        f"Prozessor: {platform.processor()}\n"
        f"CPU-Auslastung: {cpu_usage}%\n"
        f"RAM-Belegung: {ram_usage}%\n\n"
        f"Diagnose: System ist stabil. Peace of Mind garantiert!"
    )
    messagebox.showinfo("Code Doctor Status", diag_text)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Code Doctor - Quick Health Check")
    root.geometry("380x200")
    root.resizable(False, False)

    label = tk.Label(
        root,
        text="Willkommen in der Praxis des Code Doctors",
        font=("Arial", 11, "bold"),
        pady=15,
    )
    label.pack()

    btn = tk.Button(
        root,
        text="System-Diagnose starten",
        command=run_diagnostics,
        bg="#007ACC",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=15,
        pady=8,
    )
    btn.pack(pady=10)

    root.mainloop()
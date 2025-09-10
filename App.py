# app.py
import tkinter as tk
from tkinter import messagebox
import datetime

# Main window
root = tk.Tk()
root.title("IoT Garage Door Simulator")
root.geometry("450x250")

# Door state
door_state = tk.StringVar()
door_state.set("Closed")

# Action log
log_text = tk.StringVar()
log_text.set("Action Log:\n")

# Functions to open/close door
def open_door():
    if door_state.get() == "Open":
        messagebox.showinfo("Info", "Door is already open!")
    else:
        door_state.set("Open")
        status_label.config(text=f"Door Status: {door_state.get()}", fg="green")
        add_log("Door opened")

def close_door():
    if door_state.get() == "Closed":
        messagebox.showinfo("Info", "Door is already closed!")
    else:
        door_state.set("Closed")
        status_label.config(text=f"Door Status: {door_state.get()}", fg="red")
        add_log("Door closed")

def add_log(action):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_text.set(log_text.get() + f"{timestamp}: {action}\n")
    log_box.config(state="normal")
    log_box.delete(1.0, tk.END)
    log_box.insert(tk.END, log_text.get())
    log_box.config(state="disabled")

# Title label
title_label = tk.Label(root, text="IoT Garage Door Simulator", font=("Helvetica", 16))
title_label.pack(pady=10)

# Status label
status_label = tk.Label(root, text=f"Door Status: {door_state.get()}", font=("Helvetica", 14), fg="red")
status_label.pack(pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

open_button = tk.Button(button_frame, text="Open Door", width=15, command=open_door, bg="lightgreen")
open_button.grid(row=0, column=0, padx=10)

close_button = tk.Button(button_frame, text="Close Door", width=15, command=close_door, bg="lightcoral")
close_button.grid(row=0, column=1, padx=10)

# Action log box
log_label = tk.Label(root, text="Action Log:")
log_label.pack()
log_box = tk.Text(root, height=6, width=50, state="disabled")
log_box.pack(pady=5)

# Run app
root.mainloop()

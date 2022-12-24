import tkinter as tk
import time

# Create the main window
window = tk.Tk()
window.title("Alarm Clock")

# Create a label to display the current time
time_label = tk.Label(text="")
time_label.pack()

# Create a function to update the time label
def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    time_label.configure(text=current_time)
    time_label.after(1000, update_time)

# Create a function to check the alarm time
def check_alarm():
    current_time = time.strftime("%I:%M %p")
    if current_time == alarm_time.get():
        alarm_label.configure(text="ALARM")
    else:
        alarm_label.configure(text="")
        window.after(1000, check_alarm)

# Create a set time button
set_time_button = tk.Button(text="Set Alarm Time", command=check_alarm)
set_time_button.pack()

# Create an entry field for the alarm time
alarm_time = tk.Entry()
alarm_time.pack()

# Create a label to display the alarm message
alarm_label = tk.Label(text="")
alarm_label.pack()

# Update the time and start the main loop
update_time()
window.mainloop()


import tkinter as tk
from tkinter import messagebox
import subprocess

def option_selected():
    selected_option = var.get()
    if selected_option == 1:
        messagebox.showinfo("Option Selected", "You chose Option 1")
    elif selected_option == 2:
        messagebox.showinfo("Option Selected", "You chose Option 2")
    elif selected_option == 3:
        messagebox.showinfo("Option Selected", "You chose Option 3")
def callback():
    subprocess.call(["python", "usertest.py"])

# Create the main window
window = tk.Tk()
window.title("Option Selection")
window.geometry("600x400")
window.configure(bg="turquoise")

# Create a label
label = tk.Label(window, text="Welcome to our Messaging App, the MegaChat, How would You like to proceed?")
label.pack(pady=30)
label.configure(bg="turquoise")


# Create a variable to store the selected option
var = tk.IntVar()

# Create radio buttons for the options
option1 = tk.Radiobutton(window, text=" Take me to the Chat room!", variable=var, value=1)
option1.pack(pady=10)
option1.configure(bg='dodger blue')

option2 = tk.Radiobutton(window, text="I'll rather text anyone personally! ", variable=var, value=2)
option2.pack(pady=10)
option2.configure(bg='dodger blue')

option3 = tk.Radiobutton(window, text="I heard there's a bot made? Let me go have some convo with the lil friend!", variable=var, value=3)
option3.pack(pady=10)
option3.configure(bg='dodger blue')
# Create a button to confirm the selection
button = tk.Button(window, text="Select", command=callback)
button.pack(pady=10)
button.configure(fg='dark green',bg='dark green')

# Start the main loop
window.mainloop()

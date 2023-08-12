# ---------Full code to create a software application with python ---------------
 
# Import library
import tkinter as tk
 
# Create window Tkinter
window = tk.Tk()
 
# Name our Tkinter application title
window.title(" Simple Windows App ")
 
# Define window size in Tkinter python
window.geometry("700x500")
 
# Create a label widget in Tkinter
label = tk.Label(window, text="Click the Button to update this Text",
font=('Calibri 15 bold'))
label.pack(pady=20)
 
# Function to update the label text for first button click in Tkinter
def on_click_btn1():
    label["text"] = "You clicked first button"
     
# Function to update the label text for second button click in Tkinter
def on_click_btn2():
    label["text"] = "You clicked second button"
     
# Create 1st button to update the label widget
btn1 = tk.Button(window, text="Button1", command=on_click_btn1)
btn1.pack(pady=20)
 
# Create 2nd button to update the label widget
btn2 = tk.Button(window, text="Button2", command=on_click_btn2)
btn2.pack(pady=40)
 
# Run main loop
window.mainloop()
import tkinter as tk
import ttkbootstrap as ttk

def convert():
    try:
        mile_input = entry_int.get()
        km_output = mile_input * 1.61
        output_string.set(km_output)
    except:
       output_string.set("Please enter a number")

# window creation
window = ttk.Window(themename="vapor")
window.title("Converter")
window.geometry("600x300")

# tkinter variables
output_string = tk.StringVar()
entry_int = tk.IntVar()

# frames
input_frame = ttk.Frame(master=window)

# labels
title_label = ttk.Label(master=window, text="Miles to Kilometers", font="Ubuntu 24 bold")
output_label = ttk.Label(master=window, text="Output", font="Ubuntu 24", textvariable=output_string)

# entry field
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
entry.delete(0)
entry.insert(0, "")

# buttons
button = ttk.Button(master=input_frame, text="Convert", command=convert)

# packing
title_label.pack()
entry.pack(side="left", padx=10)
button.pack(side="left")
input_frame.pack(pady=10)
output_label.pack()

window.mainloop()
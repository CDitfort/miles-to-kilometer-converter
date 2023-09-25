import tkinter as tk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.609
    output_string.set(km_output)

#window
window = ttk.Window(themename='flatly')

app_name = "Miles to Kilometers"

#window title
window.title(app_name)

#width x heigh of window
window.geometry('400x200')

#label
label = ttk.Label(master = window, text = app_name,font = 'Calibri 20 bold')
label.pack(pady=10)

#Create's a frame to put widget's inside it.
input_frame = ttk.Frame(master = window)

#Set the master to input frame to set the elements inside the input_frame
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable=entry_int)

button = ttk.Button(master = input_frame,text = "Convert it!", command = convert)


#Pack the entry and the button inside the frame
entry.pack(side = 'left',padx = 5)
button.pack(side = 'left')

#Pack the input frame as well which will pack it inside the main window
input_frame.pack()

#Output
output_string = tk.StringVar()
output = ttk.Label(master = window, text = 'Output',font = 'Calibri 20', textvariable=output_string)
output.pack(padx = 5)

#run
window.mainloop()


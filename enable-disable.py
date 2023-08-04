import tkinter as tk
from tkinter import ttk

def button_func():
    entry_text = entry.get()
    
    #update the label
    #label.configure(text='some other text')
    label['text'] = entry_text
    entry['state'] = 'disabled'
    #print(label.configure())
def button2():
    label['text'] = 'some text'
    entry['state'] = 'enabled'
    

#window
window = tk.Tk()
window.title('Getting and Setting Widgets')
window.geometry('500x300')


#widgets
label = ttk.Label(master=window, text='Some text')
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text='Disabled', command = button_func)
button.pack()

otherbutton = ttk.Button(master= window, text='Enabled', command = button2)
otherbutton.pack()

window.mainloop()

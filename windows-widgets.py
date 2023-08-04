import tkinter as tk
from tkinter import ttk

def button_func():
    print('A button was pressed')
def hello():
    print('Hello')

#create window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')


#ttk label
label = ttk.Label(master=window, text='This is a text')
label.pack()

#tk text
text = tk.Text(master=window)
text.pack()

#ttk entry
entry = ttk.Entry(master = window)
entry.pack()

#exercise
text2_label = ttk.Label(master=window, text='mylabel')
text2_label.pack()


#ttk entry button
button = ttk.Button(master = window, text = 'A button', command= button_func)
button.pack()

text2 = ttk.Button(master=window, text= 'exercise button', command= lambda:print('hello'))
text2.pack()

#run 
window.mainloop()

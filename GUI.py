#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Message", "Hello, you clicked the button!")

root = tk.Tk()
root.title("Simple GUI Application")

label = tk.Label(root, text="Welcome to the Simple GUI Application")
label.pack()

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

root.mainloop()


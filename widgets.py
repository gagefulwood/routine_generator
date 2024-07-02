import tkinter as tk
from tkinter import ttk

def create_label(parent, text, row, col, sticky='w'):
    label = ttk.Label(parent, text=text)
    label.grid(row=row, column=col, sticky=sticky, padx=10)
    return label
    
def create_entry(parent, row, col):
    entry_var = tk.StringVar()
    entry = ttk.Entry(parent, textvariable=entry_var)
    entry.grid(row=row, column=col)
    return entry, entry_var

def create_combobox(parent, row, col, values=[], state="normal"):
    combo = ttk.Combobox(parent, values=values, state=state)
    if values:
        combo.set(values[0])
    combo.grid(row=row, column=col, padx=5, pady=5)
    return combo
    
def create_checkbox(parent, text, row, col, state="normal", value=False):
    check_var = tk.BooleanVar(value=value)
    check_box = ttk.Checkbutton(parent, text=text, state=state, variable=check_var)
    check_box.grid(row=row, column=col, sticky='w')
    return check_box, check_var

def create_button(parent, text, row, col, sticky='w'):
    button = ttk.Button(parent, text=text, style="Custom.TButton")
    button.grid(row=row, column=col, sticky=sticky)
    return button    
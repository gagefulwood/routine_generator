import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from model import AimTypeTag, ScenarioModel

# widgets
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



class CreateScenarioView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.model = controller.model
        self.create_widgets()

    def create_widgets(self):
        self.name_label = create_label(self,"Scenario",0,0)
        self.name_entry, self.name_var = create_entry(self,0,1)

        self.aimtype_label = create_label(self,"AimType",1,0)
        self.aimtype_combobox = create_combobox(self,1,1,values=self.model.get_aim_types())
        self.aimtype_combobox.bind("<<ComboboxSelected>>", self.update_aim_subtypes)

        self.aimsubtype_label = create_label(self,"AimSubType",2,0)
        self.aimsubtype_combobox = create_combobox(self,2,1)

        self.projectile_checkbox, self.projectile_var = create_checkbox(self,"Projectile", 3, 0)
        self.movement_checkbox, self.movement_var = create_checkbox(self,"Movement", 3, 1)
        self.flick_checkbox, self.flick_var = create_checkbox(self,"Flick", 3, 2, state="disabled")

        self.submit_btn = create_button(self,"Submit",4,1)
        self.submit_btn.bind("<Button-1>", lambda event: self.controller.submit_scenario(event,self))
    

    def update_aim_subtypes(self, event):
        aim_type = self.aimtype_combobox.get()
        aim_subtypes = self.model.get_aim_subtypes(aim_type)
        self.aimsubtype_combobox["values"] = aim_subtypes
        self.aimsubtype_combobox["state"] = "normal"
        self.aimsubtype_combobox.set(aim_subtypes[0])
        self.update_flick_checkbox(aim_type)
        
    def update_flick_checkbox(self, aim_type):
        if aim_type == AimTypeTag.CLICKING.value:
            self.flick_checkbox["state"] = "normal"
        else:
            self.flick_var.set(False)
            self.flick_checkbox["state"] = "disabled"



class ScenarioView(ttk.LabelFrame):
    def __init__(self, parent, controller, title="Scenario Frame"):
        super().__init__(parent, text=title)
        self.notebook = ttk.Notebook(self)
        self.notebook.grid()
        self.create_view = CreateScenarioView(self.notebook, controller)
        self.notebook.add(self.create_view, text="Create")

    
    
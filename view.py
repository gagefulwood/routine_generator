import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from model import AimTypeTag, ScenarioModel

SCENARIO_DIR = "scenarios"

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

class MenuView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Create widgets
        self.title_label = ttk.Label(self, text="Menu", font=("Helvetica", 18))
        self.title_label.pack(pady=10)

        self.scenario_button = ttk.Button(self, text="Manage Scenarios", command=self.open_scenario_view)
        self.scenario_button.pack(pady=5)

        self.quit_button = ttk.Button(self, text="Quit", command=self.quit_program)
        self.quit_button.pack(pady=5)

    def open_scenario_view(self):
        self.controller.open_scenario_view()

    def quit_program(self):
        self.controller.quit_program()

class ScenarioView(ttk.LabelFrame):
    def __init__(self, parent, controller, title="Scenarios"):
        super().__init__(parent, text=title)
        self.controller = controller
        self.model = controller.model
        self.create_widgets()

    def create_widgets(self):

        self.file_label = create_label(self, "Select Scenario", 0, 0)
        self.file_combobox = create_combobox(self, 0, 1, values=self.get_scenario_files())
        self.file_combobox.bind("<<ComboboxSelected>>", self.load_scenario)

        self.name_label = create_label(self,"Name",1,0)
        self.name_entry, self.name_var = create_entry(self,1,1)

        self.aimtype_label = create_label(self,"AimType",2,0)
        self.aimtype_combobox = create_combobox(self,2,1,values=self.model.get_aim_types())
        self.aimtype_combobox.bind("<<ComboboxSelected>>", self.update_aim_subtypes)

        self.aimsubtype_label = create_label(self,"AimSubType",3,0)
        self.aimsubtype_combobox = create_combobox(self,3,1)

        self.projectile_checkbox, self.projectile_var = create_checkbox(self,"Projectile", 4, 0)
        self.movement_checkbox, self.movement_var = create_checkbox(self,"Movement", 4, 1)
        self.flick_checkbox, self.flick_var = create_checkbox(self,"Flick", 4, 2, state="disabled")

        self.submit_btn = create_button(self,"Submit",5,1)
        self.submit_btn.bind("<Button-1>", lambda event: self.controller.save_scenario(event,self))
    

    def get_scenario_files(self):
        return [f for f in os.listdir(SCENARIO_DIR) if f.endswith('.json')]

    def load_scenario(self, event):
        filename = self.file_combobox.get()
        filepath = os.path.join(SCENARIO_DIR, filename)
        scenario = ScenarioModel.from_json_file(filepath)

        self.name_var.set(scenario.name)
        self.aimtype_combobox.set(scenario.aim_type)
        self.update_aim_subtypes()
        self.aimsubtype_combobox.set(scenario.aim_subtype)
        self.projectile_var.set(scenario.is_projectile)
        self.movement_var.set(scenario.is_movement)
        self.flick_var.set(scenario.is_flick)

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
        

    
    
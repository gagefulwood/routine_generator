import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from model import AimTypeTag, ScenarioModel
from widgets import *

SCENARIO_DIR = "scenarios"
PLAYLIST_DIR = "playlists"

class MenuView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Create widgets
        self.title_label = ttk.Label(self, text="Menu", font=("Helvetica", 18))
        self.title_label.pack(pady=10)

        self.scenario_button = ttk.Button(self, text="Playlists", command=self.open_playlist_view)
        self.scenario_button.pack(pady=5)

        self.scenario_button = ttk.Button(self, text="Scenarios", command=self.open_scenario_view)
        self.scenario_button.pack(pady=5)

        self.quit_button = ttk.Button(self, text="Quit", command=self.quit_program)
        self.quit_button.pack(pady=5)

    def open_scenario_view(self):
        self.controller.open_scenario_view()

    def open_playlist_view(self):
        self.controller.open_playlist_view()

    def quit_program(self):
        self.controller.quit_program()

class PlaylistView(tk.Toplevel):
    def __init__(self, parent, controller, title="Playlists"):
        super().__init__(parent)
        self.title(title)
        self.controller = controller
        self.model = controller.model
        self.create_widgets()

    def create_widgets(self):
        self.name_label = create_label(self, "Name", 0, 0)
        self.name_entry, self.name_var = create_entry(self,0,1)

        self.tracking_label = create_label(self, "Tracking", 1, 0)
        self.tracking_entry, self.tracking_var = create_entry(self, 1, 1)

        self.clicking_label = create_label(self, "Clicking", 2, 0)
        self.clicking_entry, self.clicking_var = create_entry(self, 2, 1)

        self.switching_label = create_label(self, "Switching", 3, 0)
        self.switching_entry, self.switching_var = create_entry(self, 3, 1)



class ScenarioView(tk.Toplevel):
    def __init__(self, parent, controller, title="Scenarios"):
        super().__init__(parent)
        self.title(title)
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
        

    
    
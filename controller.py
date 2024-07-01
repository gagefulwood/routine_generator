import os
import json
from tkinter import messagebox
from model import ScenarioModel

class ScenarioController:
    def __init__(self, model, save_directory="scenarios"):
        self.model = model
        self.save_directory = save_directory
        os.makedirs(self.save_directory, exist_ok=True)

    def save_scenario(self, event, create_view):
        scenario_name = create_view.name_var.get()
        aim_type = create_view.aimtype_combobox.get()
        aim_subtype = create_view.aimsubtype_combobox.get()
        projectile = create_view.projectile_var.get()
        movement = create_view.movement_var.get()
        flick = create_view.flick_var.get()

        # Create a ScenarioModel instance
        scenario = ScenarioModel(
            name=scenario_name,
            aim_type=aim_type,
            aim_subtype=aim_subtype,
            is_projectile=projectile,
            is_movement=movement,
            is_flick=flick
        )

        # Validate the scenario
        if scenario.validate():
            # Save the scenario to a JSON file
            filename = os.path.join(self.save_directory, f"{scenario_name}.json")
            scenario.to_json_file(filename)
            messagebox.showinfo("Success", f"Scenario '{scenario_name}' saved successfully!")
        else:
            messagebox.showerror("Error", "Invalid scenario data.")

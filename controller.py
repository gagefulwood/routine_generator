
from tkinter import messagebox


class ScenarioController():

    def __init__(self, model):
        self.model = model

    def submit_scenario(self, event, create_view):
        scenario_name = create_view.name_var.get()
        aim_type = create_view.aimtype_combobox.get()
        aim_subtype = create_view.aimsubtype_combobox.get()
        projectile = create_view.projectile_var.get()
        movement = create_view.movement_var.get()
        flick = create_view.flick_var.get()

        # Add your logic to handle the collected data here
        messagebox.showinfo("Scenario Data", f"Name: {scenario_name}\nAim Type: {aim_type}\nAim Subtype: {aim_subtype}\nProjectile: {projectile}\nMovement: {movement}\nFlick: {flick}")
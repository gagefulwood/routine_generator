import tkinter as tk
from tkinter import ttk
from view import ScenarioView
from model import ScenarioModel
from controller import ScenarioController

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Playlist Maker")
        self.geometry("600x400")
        self.minsize(600,400)

        model = ScenarioModel()
        controller = ScenarioController(model)
        self.scenario_view = ScenarioView(self, controller)
        self.scenario_view.grid(row=0, column=0, sticky='w')

        
        # create menus
        # create toolbars
        # create statusbar
        
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
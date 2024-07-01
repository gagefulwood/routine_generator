import tkinter as tk
from tkinter import ttk
from view import ScenarioView, MenuView
from model import ScenarioModel
from controller import ScenarioController, MenuController

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Playlist Maker")
        self.geometry("600x400")
        self.minsize(600,400)

        self.scenario_model = ScenarioModel()
        self.scenario_controller = ScenarioController(self.scenario_model)

        self.menu_controller = MenuController(self)
        self.menu_view = MenuView(self, self.menu_controller)
        self.menu_view.pack(fill=tk.BOTH, expand=True)
    
        

        
        
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
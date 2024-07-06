import tkinter as tk
from tkinter import ttk
from view import ScenarioView, MenuView
from model import PlaylistModel, ScenarioModel
from controller import PlaylistController, ScenarioController, MenuController

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Playlist Maker")
        self.geometry("400x300")
        self.minsize(400,300)

        self.playlist_model = PlaylistModel()
        self.playlist_controller = PlaylistController(self.playlist_model)

        self.scenario_model = ScenarioModel()
        self.scenario_controller = ScenarioController(self.scenario_model)

        self.menu_controller = MenuController(self)
        self.menu_view = MenuView(self, self.menu_controller)
        self.menu_view.pack(fill=tk.BOTH, expand=True)
        
        
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
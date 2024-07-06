from tkinter import ttk
from views.main_menu import MainMenuView
from views.scenario_menu import ScenarioMenuView
from views.playlist_menu import PlaylistMenuView

class MenuController:
    def __init__(self, root):
        self.root = root
        self.current_frame = None
        self.frames = {}
        self.show_frame("MainMenuView")

    def show_frame(self, view_name):
        if self.current_frame is not None:
            self.current_frame.destroy()

        if view_name in self.frames:
            frame_class = self.frames[view_name]
        else:
            frame_class = self.get_frame_class(view_name)

        self.current_frame = frame_class(parent=self.root, controller=self)
        self.current_frame.pack(fill="both", expand=True)

    def get_frame_class(self, view_name):
        if view_name == "MainMenuView":
            return MainMenuView
        elif view_name == "ScenarioMenuView":
            return ScenarioMenuView
        elif view_name == "PlaylistMenuView":
            return PlaylistMenuView
        else:
            raise ValueError(f"Unknown view: {view_name}")
        
    
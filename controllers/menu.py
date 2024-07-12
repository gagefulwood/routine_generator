from tkinter import ttk
from views.main_menu import MainMenuView
from views.scenario_menu import ScenarioMenuView
from views.playlist_menu import PlaylistMenuView
from controllers.base_model import BaseController

class MenuController(BaseController):
    def __init__(self, root):
        self.root = root
        self.current_frame = None
        self.frames = {}
        self.show_frame("MainMenuView")
    
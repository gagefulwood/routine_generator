from tkinter import ttk
from views.main_menu_view import MainMenuView
from views.scenario_menu_view import ScenarioMenuView
from views.playlist_menu_view import PlaylistMenuView
from controllers.base_controller import BaseController

class MenuController(BaseController):
    def __init__(self, root):
        self.root = root
        self.current_frame = None
        self.frames = {}
        self.show_frame("MainMenuView")
    
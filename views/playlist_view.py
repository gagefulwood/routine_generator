import tkinter as tk
from tkinter import ttk

class PlaylistView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
    def create_widgets(self):
        self.playlist_listbox = tk.Listbox(self)

import tkinter as tk
from views.playlist_view import PlaylistView

class PlaylistController:
    def __init__(self, root):
        self.root = root
        self.view = PlaylistView(root, self)
        self.name_var = tk.StringVar()
        self.tracking_var = tk.DoubleVar()
        self.clicking_var = tk.DoubleVar()
        self.switching_var = tk.DoubleVar()
        
        self.view.name_entry.config(textvariable=self.name_var)
        self.view.tracking_scale.config(variable=self.tracking_var)
        self.view.tracking_entry.config(textvariable=self.tracking_var)
        self.view.clicking_scale.config(variable=self.clicking_var)
        self.view.clicking_entry.config(textvariable=self.clicking_var)
        self.view.switching_scale.config(variable=self.switching_var)
        self.view.switching_entry.config(textvariable=self.switching_var)
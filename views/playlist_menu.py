import tkinter as tk
from tkinter import ttk

class PlaylistMenuView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.title_label = ttk.Label(self, text="Playlist Menu", font=("Helvetica", 18))
        self.title_label.pack(pady=20)

        self.import_btn = ttk.Button(self, text="Import")
        self.import_btn.config(command=None)
        self.import_btn.pack(pady=5)

        self.import_btn = ttk.Button(self, text="Create")
        self.import_btn.config(command=None)
        self.import_btn.pack(pady=5)

        self.import_btn = ttk.Button(self, text="Edit")
        self.import_btn.config(command=None)
        self.import_btn.pack(pady=5)

        self.back_btn = ttk.Button(self, text="Back")
        self.back_btn.config(command=lambda: self.controller.show_frame("MainMenuView"))
        self.back_btn.pack(pady=10)
    

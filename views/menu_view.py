import tkinter as tk
from tkinter import ttk

class MenuView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.title_label = ttk.Label(self, text="Main Menu", font=("Helvetica", 18))
        self.title_label.pack(pady=20)

        self.scenarios_btn = ttk.Button(self, text="Scenarios")
        self.scenarios_btn.config(command=None)
        self.scenarios_btn.pack(pady=5)

        self.playlists_btn = ttk.Button(self, text="Playlists")
        self.playlists_btn.config(command=None)
        self.playlists_btn.pack(pady=5)

        self.settings_btn = ttk.Button(self, text="Settings")
        self.settings_btn.config(command=None)
        self.settings_btn.pack(pady=5)

        self.exit_btn = ttk.Button(self, text="Exit")
        self.exit_btn.config(command=None)
        self.exit_btn.pack(pady=20)
        

        
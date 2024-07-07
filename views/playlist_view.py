import tkinter as tk
from tkinter import ttk

class PlaylistView(ttk.LabelFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, text="Playlist Maker")
        self.controller = controller
        self.pack(expand=True, fill="both")
        self.create_widgets()
        
        
    def create_widgets(self):
        self.name = ttk.Label(self,text="Name:")
        self.name.grid(row=0,column=0)
        self.name_entry = ttk.Entry(self, width=30)
        self.name_entry.grid(row=0,column=1)

        self.tracking_label = ttk.Label(self,text="Tracking:")
        self.tracking_label.grid(row=1,column=0)
        self.tracking_scale = ttk.Scale(self, from_=0, to=100,
                                        orient=tk.HORIZONTAL,
                                        length=200)
        self.tracking_scale.grid(row=1,column=1)
        self.tracking_entry = ttk.Entry(self, width=4)
        self.tracking_entry.grid(row=1,column=2)


        self.clicking_label = ttk.Label(self,text="Clicking:")
        self.clicking_label.grid(row=2,column=0)
        self.clicking_scale = ttk.Scale(self, from_=0, to=100,
                                        orient=tk.HORIZONTAL,
                                        length=200)
        self.clicking_scale.grid(row=2,column=1)
        self.clicking_entry = ttk.Entry(self, width=4)
        self.clicking_entry.grid(row=2,column=2)


        self.switching_label = ttk.Label(self,text="Switching:")
        self.switching_label.grid(row=3,column=0)
        self.switching_scale = ttk.Scale(self, from_=0, to=100,
                                        orient=tk.HORIZONTAL,
                                        length=200)
        self.switching_scale.grid(row=3,column=1)
        self.switching_entry = ttk.Entry(self, width=4)
        self.switching_entry.grid(row=3,column=2)
        

        self.generate_btn = ttk.Button(self, text="Generate")
        self.generate_btn.grid(row=5,column=1)

        self.scenario_listbox = tk.Listbox(self, width=65, height=9)
        self.scenario_listbox.grid(row=6,column=0,columnspan=4)
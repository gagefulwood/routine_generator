from tkinter import ttk

class ScenarioView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.model = controller.model
        self.create_widgets()

    def create_widgets(self):
        pass
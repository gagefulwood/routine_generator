import tkinter as tk
from controllers.menu_controller import MenuController

'''
create model instance
create controller instance
'''

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TBD") #TBD title
        self.geometry("400x300")
        self.minsize(400,300)

        #init controllers
        self.controllers = [ MenuController(self) ]

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
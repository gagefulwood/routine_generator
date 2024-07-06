import tkinter as tk
from controllers.menu import MenuController

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

        #init models

        #init views

        #init controllers
        self.menu_controller = MenuController(self)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
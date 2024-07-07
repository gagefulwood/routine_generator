import tkinter as tk
from views.menu_view import MenuView
from controllers.menu_controller import MenuController

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TBD") #TBD title
        self.geometry("400x300")
        self.minsize(400,300)

        self.current_view = None
        self.current_controller = None

        self.switch_view(MenuController)

    def switch_view(self, controller_class):
        if self.current_view is not None:
            self.current_view.pack_forget()
        self.current_controller = controller_class(self)
        self.current_view = self.current_controller.view
        self.current_view.pack()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
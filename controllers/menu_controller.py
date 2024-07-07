from views.menu_view import MenuView
from views.scenario_view import ScenarioView
from controllers.scenario_controller import ScenarioController
from views.playlist_view import PlaylistView
from controllers.playlist_controller import PlaylistController
from views.settings_view import SettingsView
from controllers.settings_controller import SettingsController

class MenuController:
    def __init__(self, root):
        self.root = root
        self.view = MenuView(root, self)

        self.view.scenarios_btn.config(command=self.show_scenario_view)
        self.view.playlists_btn.config(command=self.show_playlist_view)
        self.view.settings_btn.config(command=self.show_settings_view)
        self.view.exit_btn.config(command=self.exit_application)
    
    def show_scenario_view(self):
        self.root.switch_view(ScenarioController)

    def show_playlist_view(self):
        self.root.switch_view(PlaylistController)

    def show_settings_view(self):
        self.root.switch_view(SettingsController)

    def exit_application(self):
        self.root.destroy()

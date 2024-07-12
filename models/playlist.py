from models.base_model import BaseModel

class PlaylistModel(BaseModel):

    def __init__(self, playlist_id, name, description, num_scenarios, clicking_proportion, tracking_proportion, target_switching_proportion, other_proportion):
        self.playlist_id = playlist_id
        self.name = name
        self.description = description
        self.num_scenarios = num_scenarios
        self.clicking_proportion = clicking_proportion
        self.tracking_proportion = tracking_proportion
        self.target_switching_proportion = target_switching_proportion
        self.other_proportion = other_proportion
        self.validate()

    def validate(self):
        if not isinstance(self.playlist_id, int):
            raise TypeError("playlist_id must be an integer")
        if self.playlist_id < 0:
            raise ValueError("playlist_id must be nonnegative")
        if not isinstance(self.name, str):
            raise TypeError("name must be a string")
        if not isinstance(self.description, str):
            raise TypeError("description must be a string")
        if not isinstance(self.num_scenarios, int):
            raise TypeError("num_scenarios must be an integer")
        if not isinstance(self.clicking_proportion, (int, float)):
            raise TypeError("clicking_proportion must be a number")
        if not 0 <= self.clicking_proportion <= 1:
            raise ValueError("clicking_proportion must be between 0 and 1")
        if not isinstance(self.tracking_proportion, (int, float)):
            raise TypeError("tracking_proportion must be a number")
        if not 0 <= self.tracking_proportion <= 1:
            raise ValueError("tracking_proportion must be between 0 and 1")
        if not isinstance(self.target_switching_proportion, (int, float)):
            raise TypeError("target_switching_proportion must be a number")
        if not 0 <= self.target_switching_proportion <= 1:
            raise ValueError("target_switching_proportion must be between 0 and 1")
        if not isinstance(self.other_proportion, (int, float)):
            raise TypeError("other_proportion must be a number")
        if not 0 <= self.other_proportion <= 1:
            raise ValueError("other_proportion must be between 0 and 1")
        
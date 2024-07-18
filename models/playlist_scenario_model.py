from models.base_model import BaseModel

class PlaylistScenarioModel(BaseModel):

    def __init__(self, playlist_id, scenario_id, num_reps):
        self.playlist_id = playlist_id
        self.scenario_id = scenario_id
        self.num_reps = num_reps
        self.validate()

    def validate(self):
        if not isinstance(self.playlist_id, int):
            raise TypeError("playlist_id must be an integer")
        if self.playlist_id < 0:
            raise ValueError("playlist_id must be nonnegative")
        if not isinstance(self.scenario_id, int):
            raise TypeError("scenario_id must be an integer")
        if self.scenario_id < 0:
            raise ValueError("scenario_id must be nonnegative")
        if not isinstance(self.num_reps, int):
            raise TypeError("num_reps must be an integer")
        if self.num_reps <= 0:
            raise ValueError("num_reps must be positive")
        
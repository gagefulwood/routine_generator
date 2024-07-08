class PlaylistScenarioModel:

    def __init__(self, playlist_id, scenario_id, num_reps):
        self.validate(playlist_id, scenario_id, num_reps)
        self.playlist_id = playlist_id
        self.scenario_id = scenario_id
        self.num_reps = num_reps

    def validate(playlist_id, scenario_id, num_reps):
        if not isinstance(playlist_id, int):
            raise TypeError("playlist_id must be an integer")
        if playlist_id < 0:
            raise ValueError("playlist_id must be nonnegative")
        if not isinstance(scenario_id, int):
            raise TypeError("scenario_id must be an integer")
        if scenario_id < 0:
            raise ValueError("scenario_id must be nonnegative")
        if not isinstance(num_reps, int):
            raise TypeError("num_reps must be an integer")
        if num_reps <= 0:
            raise ValueError("num_reps must be positive")
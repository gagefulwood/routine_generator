class PlaylistModel:

    def __init__(self, name, description, num_scenarios):
        self.validate(name, description, num_scenarios)
        self.name = name
        self.description = description
        self.num_scenarios = num_scenarios

    def validate(playlist_id, name, description, num_scenarios):
        if not isinstance(playlist_id, int):
            raise TypeError("playlist_id must be an integer")
        if playlist_id < 0:
            raise ValueError("playlist_id must be nonnegative")
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(description, str):
            raise TypeError("description must be a string")
        if not isinstance(num_scenarios, int):
            raise TypeError("num_scenarios must be an integer")
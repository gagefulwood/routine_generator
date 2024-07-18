import csv
from .playlist_model import PlaylistModel

class PlaylistManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.playlists = []
        self.load_playlists()

    def load_playlists(self):
        with open(self.csv_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                playlist = PlaylistModel(
                    int(row['playlist_id']),
                    row['name'],
                    row['description'],
                    int(row['num_scenarios']),
                    float(row['clicking_proportion']),
                    float(row['tracking_proportion']),
                    float(row['target_switching_proportion']),
                    float(row['other_proportion'])
                )
                self.playlists.append(playlist)

    def save_playlists(self):
        with open(self.csv_file, mode='w', newline='') as file:
            fieldnames = ['playlist_id', 'name', 'description', 'num_scenarios', 'clicking_proportion', 'tracking_proportion', 'target_switching_proportion', 'other_proportion']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for playlist in self.playlists:
                writer.writerow({
                    'playlist_id': playlist.playlist_id,
                    'name': playlist.name,
                    'description': playlist.description,
                    'num_scenarios': playlist.num_scenarios,
                    'clicking_proportion': playlist.clicking_proportion,
                    'tracking_proportion': playlist.tracking_proportion,
                    'target_switching_proportion': playlist.target_switching_proportion,
                    'other_proportion': playlist.other_proportion
                })

    def add_playlist(self, playlist):
        self.playlists.append(playlist)
        self.save_playlists()

    def update_playlist(self, playlist_id, new_data):
        for playlist in self.playlists:
            if playlist.playlist_id == playlist_id:
                for key, value in new_data.items():
                    setattr(playlist, key, value)
                self.save_playlists()
                return True
        return False

    def delete_playlist(self, playlist_id):
        self.playlists = [playlist for playlist in self.playlists if playlist.playlist_id != playlist_id]
        self.save_playlists()

    def get_playlist_by_id(self, playlist_id):
        for playlist in self.playlists:
            if playlist.playlist_id == playlist_id:
                return playlist
        return None

    def get_all_playlists(self):
        return self.playlists

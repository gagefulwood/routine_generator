import csv
from playlist_scenario_model import PlaylistScenarioModel

class PlaylistScenarioManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.scenarios = []
        self.load_scenarios()

    def load_scenarios(self):
        with open(self.csv_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                scenario = PlaylistScenarioModel(
                    int(row['playlist_id']),
                    int(row['scenario_id']),
                    int(row['num_reps'])
                )
                self.scenarios.append(scenario)

    def save_scenarios(self):
        with open(self.csv_file, mode='w', newline='') as file:
            fieldnames = ['playlist_id', 'scenario_id', 'num_reps']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for scenario in self.scenarios:
                writer.writerow({
                    'playlist_id': scenario.playlist_id,
                    'scenario_id': scenario.scenario_id,
                    'num_reps': scenario.num_reps
                })

    def add_scenario(self, scenario):
        self.scenarios.append(scenario)
        self.save_scenarios()

    def update_scenario(self, playlist_id, scenario_id, new_data):
        for scenario in self.scenarios:
            if scenario.playlist_id == playlist_id and scenario.scenario_id == scenario_id:
                for key, value in new_data.items():
                    setattr(scenario, key, value)
                self.save_scenarios()
                return True
        return False

    def delete_scenario(self, playlist_id, scenario_id):
        self.scenarios = [scenario for scenario in self.scenarios if not (scenario.playlist_id == playlist_id and scenario.scenario_id == scenario_id)]
        self.save_scenarios()

    def get_scenario_by_id(self, playlist_id, scenario_id):
        for scenario in self.scenarios:
            if scenario.playlist_id == playlist_id and scenario.scenario_id == scenario_id:
                return scenario
        return None

    def get_all_scenarios(self):
        return self.scenarios

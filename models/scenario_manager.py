import csv
from .scenario_model import ScenarioModel
from enums.aim_type import AimType
from enums.aim_subtype import AimSubType

class ScenarioManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.scenarios = []
        self.load_scenarios()

    def load_scenarios(self):
        with open(self.csv_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                scenario = ScenarioModel(
                    int(row['scenario_id']),
                    row['name'],
                    AimType[row['aim_type']],
                    AimSubType[row['aim_subtype']],
                    row['is_projectile'].lower() == 'true',
                    row['is_movement'].lower() == 'true',
                    row['is_flick'].lower() == 'true'
                )
                self.scenarios.append(scenario)

    def save_scenarios(self):
        with open(self.csv_file, mode='w', newline='') as file:
            fieldnames = ['scenario_id', 'name', 'aim_type', 'aim_subtype', 'is_projectile', 'is_movement', 'is_flick']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for scenario in self.scenarios:
                writer.writerow({
                    'scenario_id': scenario.scenario_id,
                    'name': scenario.name,
                    'aim_type': scenario.aim_type.name,
                    'aim_subtype': scenario.aim_subtype.name,
                    'is_projectile': scenario.is_projectile,
                    'is_movement': scenario.is_movement,
                    'is_flick': scenario.is_flick
                })

    def add_scenario(self, scenario):
        # Assuming scenario is an instance of ScenarioModel
        self.scenarios.append(scenario)
        self.save_scenarios()

    def update_scenario(self, scenario_id, new_data):
        for scenario in self.scenarios:
            if scenario.scenario_id == scenario_id:
                for key, value in new_data.items():
                    setattr(scenario, key, value)
                self.save_scenarios()
                return True
        return False

    def delete_scenario(self, scenario_id):
        self.scenarios = [scenario for scenario in self.scenarios if scenario.scenario_id != scenario_id]
        self.save_scenarios()

    def get_scenario_by_id(self, scenario_id):
        for scenario in self.scenarios:
            if scenario.scenario_id == scenario_id:
                return scenario
        return None

    def get_all_scenarios(self):
        return self.scenarios

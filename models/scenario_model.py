from enum import Enum

class AimType(Enum):
    TRACKING = "Tracking"
    CLICKING = "Clicking"
    SWITCHING = "Target Switching"
    OTHER = "Other"

class AimSubType(Enum):
    SMOOTHNESS = "Smoothness"
    REACTIVITY = "Reactivity"
    STATIC = "Static"
    DYNAMIC = "Dynamic"
    SLOW = "Slow"
    FAST = "Fast"
    BOTH = "Both"
    OTHER = "Other"

valid_subtypes = {
    AimType.TRACKING: [AimSubType.SMOOTHNESS, AimSubType.REACTIVITY, AimSubType.BOTH, AimSubType.OTHER],
    AimType.CLICKING: [AimSubType.STATIC, AimSubType.DYNAMIC, AimSubType.BOTH, AimSubType.OTHER],
    AimType.SWITCHING: [AimSubType.SLOW, AimSubType.FAST, AimSubType.BOTH, AimSubType.OTHER],
    AimType.OTHER: [],
}

class ScenarioModel:

    def __init__(self, name, aim_type, aim_subtype, is_projectile, is_movement, is_flick):
        self.validate(name, aim_type, aim_subtype, is_projectile, is_movement, is_flick)
        self.name = name
        self.aim_type = aim_type
        self.aim_subtype = aim_subtype
        self.is_projectile = is_projectile
        self.is_movement = is_movement
        self.is_flick = is_flick

    @classmethod
    def validate(cls, name, aim_type, aim_subtype, is_projectile, is_movement, is_flick):
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        if not isinstance(aim_type, AimType):
            raise ValueError("aim_type must be an AimType enum member")
        if not isinstance(aim_subtype, AimSubType):
            raise ValueError("aim_subtype must be an AimSubType enum member")
        if not isinstance(is_projectile, bool):
            raise ValueError("is_projectile must be a boolean")
        if not isinstance(is_movement, bool):
            raise ValueError("is_movement must be a boolean")
        if not isinstance(is_flick, bool):
            raise ValueError("is_flick must be a boolean")
        if aim_subtype not in valid_subtypes.get(aim_type):
            raise ValueError(f"Invalid aim_subtype combination for {aim_type.name}")
        if is_flick and aim_type != AimType.CLICKING:
            is_flick = False

    def create_scenario(self): # inserts scenario into the database
        pass

    def update_scenario(self): # update an existing scenario in the database
        pass

    @classmethod
    def read_scenario(cls, scenario_id): # retrieves a scenario from the database
        pass

    @classmethod
    def delete_scenario(cls, scenario_id): # deletes a scenario from the database by its ID
        pass
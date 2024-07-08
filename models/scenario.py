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

    def validate(scenario_id, name, aim_type, aim_subtype, is_projectile, is_movement, is_flick):
        if not isinstance(scenario_id, int):
            raise TypeError("scenario_id must be an integer")
        if scenario_id < 0:
            raise ValueError("scenario_id must be nonnegative")
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(aim_type, AimType):
            raise TypeError("aim_type must be an AimType enum member")
        if not isinstance(aim_subtype, AimSubType):
            raise TypeError("aim_subtype must be an AimSubType enum member")
        if not isinstance(is_projectile, bool):
            raise TypeError("is_projectile must be a boolean")
        if not isinstance(is_movement, bool):
            raise TypeError("is_movement must be a boolean")
        if not isinstance(is_flick, bool):
            raise TypeError("is_flick must be a boolean")
        if aim_subtype not in valid_subtypes.get(aim_type):
            raise ValueError(f"Invalid aim_subtype combination for {aim_type.name}")
        if is_flick and aim_type != AimType.CLICKING:
            is_flick = False

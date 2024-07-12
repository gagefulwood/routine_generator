from enums.aim_type import AimType
from enums.aim_subtype import AimSubType

class ScenarioModel:
    
    valid_subtypes = {
        AimType.TRACKING: [AimSubType.SMOOTHNESS, AimSubType.REACTIVITY, AimSubType.BOTH, AimSubType.OTHER],
        AimType.CLICKING: [AimSubType.STATIC, AimSubType.DYNAMIC, AimSubType.BOTH, AimSubType.OTHER],
        AimType.SWITCHING: [AimSubType.SLOW, AimSubType.FAST, AimSubType.BOTH, AimSubType.OTHER],
        AimType.OTHER: [],
    }

    def __init__(self, scenario_id, name, aim_type, aim_subtype, is_projectile, is_movement, is_flick):
        self.name = name
        self.scenario_id = scenario_id
        self.aim_type = aim_type
        self.aim_subtype = aim_subtype
        self.is_projectile = is_projectile
        self.is_movement = is_movement
        self.is_flick = is_flick
        self.validate()

    def validate(self):
        if not isinstance(self.scenario_id, int):
            raise TypeError("scenario_id must be an integer")
        if self.scenario_id < 0:
            raise ValueError("scenario_id must be nonnegative")
        if not isinstance(self.name, str):
            raise TypeError("name must be a string")
        if not isinstance(self.aim_type, AimType):
            raise TypeError("aim_type must be an AimType enum member")
        if not isinstance(self.aim_subtype, AimSubType):
            raise TypeError("aim_subtype must be an AimSubType enum member")
        if not isinstance(self.is_projectile, bool):
            raise TypeError("is_projectile must be a boolean")
        if not isinstance(self.is_movement, bool):
            raise TypeError("is_movement must be a boolean")
        if not isinstance(self.is_flick, bool):
            raise TypeError("is_flick must be a boolean")
        if self.aim_subtype not in self.valid_subtypes.get(self.aim_type):
            raise ValueError(f"Invalid aim_subtype combination for {self.aim_type.name}")
        if is_flick and self.aim_type != AimType.CLICKING:
            is_flick = False

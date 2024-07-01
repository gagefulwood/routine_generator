from enum import Enum
import json

class AimTypeTag(Enum):
    TRACKING = "Tracking"
    CLICKING = "Clicking"
    TARGET_SWITCHING = "Target Switching"
    OTHER = "Other"

class AimSubTypeTag(Enum):
    SMOOTHNESS = "Smoothness"
    REACTIVITY = "Reactivity"
    STATIC = "Static"
    DYNAMIC = "Dynamic"
    SLOW = "Slow"
    FAST = "Fast"
    BOTH = "Both"
    OTHER = "Other"


class ScenarioModel:
    aim_subtype_mapping = {
        AimTypeTag.TRACKING.value: [AimSubTypeTag.SMOOTHNESS.value, AimSubTypeTag.REACTIVITY.value, AimSubTypeTag.BOTH.value, AimSubTypeTag.OTHER.value],
        AimTypeTag.CLICKING.value: [AimSubTypeTag.DYNAMIC.value, AimSubTypeTag.STATIC.value, AimSubTypeTag.BOTH.value, AimSubTypeTag.OTHER.value],
        AimTypeTag.TARGET_SWITCHING.value: [AimSubTypeTag.STATIC.value, AimSubTypeTag.SLOW.value, AimSubTypeTag.FAST.value, AimSubTypeTag.OTHER.value],
        AimTypeTag.OTHER.value: [AimSubTypeTag.OTHER.value]
    }

    def __init__(self, name = None, aim_type=AimTypeTag.OTHER.value, aim_subtype=AimSubTypeTag.OTHER.value,
                is_projectile=False, is_movement=False, is_flick=False):
        self.name = name
        self.aim_type = aim_type
        self.aim_subtype = aim_subtype
        self.is_projectile = is_projectile
        self.is_movement = is_movement
        self.is_flick = is_flick

    def validate(self):
        if self.aim_type in AimTypeTag.__members__.values():
            if self.aim_type == AimTypeTag.TRACKING.value:
                return self.aim_subtype in self.aim_subtype_mapping.get(AimTypeTag.TRACKING.value, []) and not self.is_flick
            elif self.aim_type == AimTypeTag.CLICKING.value:
                return self.aim_subtype in self.aim_subtype_mapping.get(AimTypeTag.CLICKING.value, [])
            elif self.aim_type == AimTypeTag.TARGET_SWITCHING.value:
                return self.aim_subtype in self.aim_subtype_mapping.get(AimTypeTag.TARGET_SWITCHING.value, []) and not self.is_flick
            else:
                return True #later make this handle the other condition
        return False
    
    def to_dict(self):
        return {
            "Name": self.name,
            "AimTypeTag": self.aim_type,
            "AimSubTypeTag": self.aim_subtype,
            "AimTypeProjectile": self.is_projectile,
            "AimTypePlayerMovement": self.is_movement,
            "AimTypeFlick": self.is_flick
        }
    
    def to_json_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.to_dict(), file, indent=4)
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            name = data.get("Name"),
            aim_type = data.get("AimTypeTag", AimTypeTag.OTHER.value),
            aim_subtype = data.get("AimSubTypeTag", AimTypeTag.OTHER.value),
            is_projectile = data.get("AimTypeProjectile", False),
            is_movement = data.get("AimTypePlayerMovement", False),
            is_flick = data.get("AimTypeFlick", False)
            )

    @classmethod
    def from_json_file(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return cls.from_dict(data)
    
    def get_aim_types(self):
        return list(self.aim_subtype_mapping.keys())

    def get_aim_subtypes(self, aim_type):
        return self.aim_subtype_mapping.get(aim_type, [])
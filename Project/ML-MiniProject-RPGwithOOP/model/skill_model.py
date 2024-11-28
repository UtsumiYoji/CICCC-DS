from typing import Literal


class Skill():
    hp = 0
    mp = 0
    target_num = 1
    target_type: Literal["enemy", "party", "itself"] = "enemy"
    affect_to = "hp"
    formula:str = ""
    defense_formula:str = ""
    skill_type: Literal["attack",  "buff", "debuff"] = "attack"
    buff_duration = 0


class Attack(Skill):
    name = "Attack"
    formula = "1 * attack_power + 5"
    defense_formula = "attack_defense"


class Block(Skill):
    target_num = 1
    name = "Block"
    target_type = "itself"
    affect_to = "attack_defense"
    formula = "attack_defense * 1.5"
    skill_type = "buff"
    buff_duration = 1


class FireBall(Skill):
    name = "Fire Ball"
    mp = 5
    formula = "1 * magic_power * 2 + 3"
    defense_formula = "magic_defense"


class DoubleFireBall(Skill):
    name = "Double Fire Ball"
    mp = 8
    target_num = 2
    formula = "1 * magic_power * 2 + 5"
    defense_formula = "magic_defense"


class TripleFireBall(Skill):
    name = "Triple Fire Ball"
    mp = 12
    target_num = 3
    formula = "1 * magic_power * 2 + 7"
    defense_formula = "magic_defense"


class FireBallRain(Skill):
    name = "Fire Ball Rain"
    mp = 20
    target_num = 99
    formula = "1 * magic_power * 2.2 + 10"
    

class Heal(Skill):
    name = "Heal"
    mp = 5
    target_type = "party"
    formula = "magic_power * 1.2 + 3"
    skill_type = "buff"


class MegaHeal(Skill):
    name = "Mega Heal"
    mp = 10
    target_type = "party"
    formula = "magic_power * 1.5 + 5"
    skill_type = "buff"


class GigaHeal(Skill):
    name = "Giga Heal"
    mp = 15
    target_type = "party"
    formula = "magic_power * 2 + 10"
    skill_type = "buff"


class HealAll(Skill):
    name = "Heal All"
    mp = 8
    target_type = "party"
    target_num = 99
    formula = "magic_power * 1.1 + 3"
    skill_type = "buff"
    

class MegaHealAll(Skill):
    name = "Mega Heal All"
    mp = 15
    target_type = "party"
    target_num = 99
    formula = "magic_power * 1.3 + 5"
    skill_type = "buff"
    

class GigaHealAll(Skill):
    name = "Giga Heal All"
    mp = 20
    target_type = "party"
    target_num = 99
    formula = "magic_power * 1.7 + 10"
    skill_type = "buff"


class ThunderStrike(Skill):
    name = "Thunder Strike"
    mp = 7
    formula = "1 * magic_power * 2.5 + 4"
    defense_formula = "magic_defense"


class IceShard(Skill):
    name = "Ice Shard"
    mp = 10
    formula = "1 * magic_power * 2 + 3"
    affect_to = "defense"
    skill_type = "buff"
    buff_duration = 1


class EarthQuake(Skill):
    name = "Earth Quake"
    mp = 15
    target_num = 99
    formula = "1 * attack_power * 2.5 + 10"
    defense_formula = "attack_defense"


class Shield(Skill):
    name = "Shield"
    mp = 8
    target_type = "itself"
    affect_to = "defense"
    formula = "defense * 2"
    skill_type = "buff"
    buff_duration = 1

    
class Slash(Skill):
    name = "Slash"
    mp = 3
    formula = "1 * attack_power * 1.5 + 2"
    defense_formula = "attack_defense"


class PowerStrike(Skill):
    name = "Power Strike"
    mp = 5
    formula = "1 * attack_power * 2 + 4"
    defense_formula = "attack_defense"


class LightningBlade(Skill):
    name = "Lightning Blade"
    mp = 10
    formula = "1 * attack_power * 2.5 + 6"
    defense_formula = "attack_defense"


class PoisonDart(Skill):
    name = "Poison Dart"
    mp = 4
    formula = "1 * attack_power * 1.2 + 3"
    defense_formula = "attack_defense"


class WindSlash(Skill):
    name = "Wind Slash"
    mp = 6
    formula = "1 * attack_power * 1.8 + 4"
    defense_formula = "attack_defense"


class WaterBlast(Skill):
    name = "Water Blast"
    mp = 7
    formula = "1 * magic_power * 2.2 + 5"
    defense_formula = "magic_defense"


class StoneThrow(Skill):
    name = "Stone Throw"
    mp = 3
    formula = "1 * attack_power * 1.3 + 2"
    defense_formula = "attack_defense"


class DarkPulse(Skill):
    name = "Dark Pulse"
    mp = 12
    target_num = 99
    formula = "1 * magic_power * 2.8 + 6"
    defense_formula = "magic_defense"


class LightBeam(Skill):
    name = "Light Beam"
    mp = 10
    formula = "1 * magic_power * 2.5 + 5"
    defense_formula = "magic_defense"


class FrostBite(Skill):
    name = "Frost Bite"
    mp = 8
    formula = "1 * magic_power * 2.3 + 4"
    defense_formula = "magic_defense"


class FlameBurst(Skill):
    name = "Flame Burst"
    mp = 9
    formula = "1 * magic_power * 2.6 + 5"
    defense_formula = "magic_defense"


class EarthShield(Skill):
    name = "Earth Shield"
    mp = 10
    target_type = "itself"
    affect_to = "defense"
    formula = "defense * 2.5"
    skill_type = "buff"
    buff_duration = 2


class AquaHeal(Skill):
    name = "Aqua Heal"
    mp = 6
    target_type = "party"
    formula = "magic_power * 1.3 + 4"
    skill_type = "buff"
    buff_duration = 2


class Inferno(Skill):
    name = "Inferno"
    mp = 20
    target_num = 99
    formula = "1 * magic_power * 4 + 10"
    defense_formula = "magic_defense"


class Tornado(Skill):
    name = "Tornado"
    mp = 18
    target_num = 99
    formula = "1 * magic_power * 2.7 + 8"
    defense_formula = "magic_defense"


class MeteorShower(Skill):
    name = "Meteor Shower"
    mp = 25
    target_num = 99
    formula = "1 * magic_power * 3.5 + 12"
    defense_formula = "magic_defense"


class HolyLight(Skill):
    name = "Holy Light"
    mp = 15
    target_type = "party"
    formula = "magic_power * 2 + 8"
    skill_type = "buff"


class ShadowStrike(Skill):
    name = "Shadow Strike"
    mp = 10
    formula = "1 * attack_power * 3 + 5"
    defense_formula = ""
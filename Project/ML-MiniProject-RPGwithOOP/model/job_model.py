from abc import abstractmethod
import random

from model.model import Model
from model.skill_model import *


class BaseJob(Model):
    NEED_EXP_TO_LEVEL_UP = [
        0, 12, 30, 57, 98, 158, 249, 386, 591, 899, 1360, 2052,
        3090, 4647, 6982, 10485, 15740, 23622, 35445, 53180, 79782,
        119685, 179540, 269322, 403995, 606004, 909018, 1363539,
        2045321, 3067993, 4602001, 6903014, 10354533, 15531812,
        23297730, 34946607, 52419922, 78629895, 117944854, 176917293,
    ]
    
    @property
    @abstractmethod
    def BASE_HP(self):
        pass
    
    @property
    @abstractmethod
    def BASE_MP(self):
        pass
    
    @property
    @abstractmethod
    def BASE_ATTACK_POWER(self):
        pass
    
    @property
    @abstractmethod
    def BASE_MAGIC_POWER(self):
        pass
    
    @property
    @abstractmethod
    def BASE_ATTACK_DEFENSE(self):
        pass
    
    @property
    @abstractmethod
    def BASE_MAGIC_DEFENSE(self):
        pass
    
    @property
    @abstractmethod
    def BASE_SPEED(self):
        pass
    
    @property
    @abstractmethod
    def BASE_LUCK(self):
        pass
    
    @property
    @abstractmethod
    def FEATURES(self):
        pass
    
    @property
    @abstractmethod
    def LEVEL_UP_RANGE(self):
        pass
    
    @property
    @abstractmethod
    def SKILL_ACQUISITION(self):
        pass
    
    @classmethod
    def first_status(cls) -> dict:
        return {
            'HP': cls.BASE_HP,
            'MP': cls.BASE_MP,
            'Attack-power': cls.BASE_ATTACK_POWER,
            'Magic-power': cls.BASE_MAGIC_POWER,
            'Attack-defense': cls.BASE_ATTACK_DEFENSE,
            'Magic-defense': cls.BASE_MAGIC_DEFENSE,
            'Speed': cls.BASE_SPEED,
            'Luck': cls.BASE_LUCK
        }
    
    def __init__(self, name: str) -> None:
        super().__init__(name)
        # First status
        self.hp = self.BASE_HP
        self.mp = self.BASE_MP
        self.attack_power = self.BASE_ATTACK_POWER
        self.magic_power = self.BASE_MAGIC_POWER
        self.attack_defense = self.BASE_ATTACK_DEFENSE
        self.magic_defense = self.BASE_MAGIC_DEFENSE
        self.speed = self.BASE_SPEED
        self.luck = self.BASE_LUCK
        
        # First level and experience
        self.level = 1
        self.exp = 0
        
        # skills
        self.skills = self.SKILL_ACQUISITION.get(0, []).copy()
        
        # store status as a current status
        self.c_hp = self.hp
        self.c_mp = self.mp
        self.c_attack_power = self.attack_power
        self.c_magic_power = self.magic_power
        self.c_attack_defense = self.attack_defense
        self.c_magic_defense = self.magic_defense
        self.c_speed = self.speed
        self.c_luck = self.luck
        
        # buffer
        self.buff_buffer = list()
    
    def get_status(self):
        return {
            'Name': self.name,
            'Level': self.level,
            'HP': self.hp,
            'MP': self.mp,
            'Attack-power': self.attack_power,
            'Magic-power': self.magic_power,
            'Attack-defense': self.attack_defense,
            'Magic-defense': self.magic_defense,
            'Speed': self.speed,
            'Luck': self.luck
        }
    
    def level_up(self):
        for status, value in self.LEVEL_UP_RANGE.items():
            if random.randint(1, 100) <= value["chance"]:
                setattr(self, status, getattr(self, status) + random.randint(value["min"], value["max"]))
        
        self.level += 1
        new_skills = self.SKILL_ACQUISITION.get(self.level, [])
        self.skills += new_skills
        
        return new_skills
    
    def get_exp(self, exp:int):
        before = self.get_status()
        
        self.exp += exp
        for level, need_exp in enumerate(self.NEED_EXP_TO_LEVEL_UP, 1):
            if self.exp < need_exp:
                break
        
        new_skills = []
        for _ in range(self.level, level):
            new_skills += self.level_up()
        
        return before, self.get_status(), new_skills


class Warrior(BaseJob):
    BASE_HP = 50
    BASE_MP = 10
    BASE_ATTACK_POWER = 20
    BASE_MAGIC_POWER = 5
    BASE_ATTACK_DEFENSE = 10
    BASE_MAGIC_DEFENSE = 2
    BASE_SPEED = 5
    BASE_LUCK = 2
    FEATURES = [
        "It has high attack-power and physical-defense",
        "It doesn't have good magic-power and magic-defense",
        "It can be main party member in charge of an attack"
    ]
    
    LEVEL_UP_RANGE = {
        "hp" : {"min":5, "max":7, "chance":100},
        "mp" : {"min":1, "max":3, "chance":100},
        "attack_power" : {"min":3, "max":5, "chance":100},
        "magic_power" : {"min":0, "max":2, "chance":100},
        "attack_defense" : {"min":2, "max":4, "chance":100},
        "magic_defense" : {"min":0, "max":2, "chance":100},
        "speed" : {"min":1, "max":1, "chance":50},
        "luck" : {"min":1, "max":1, "chance":20},
    }
    
    SKILL_ACQUISITION = {
        0: [Slash],
        5: [PowerStrike],
        7: [Shield],
        10: [LightningBlade],
        13: [EarthShield],
        18: [ShadowStrike],
    }

class Wizard(BaseJob):
    BASE_HP = 40
    BASE_MP = 35
    BASE_ATTACK_POWER = 5
    BASE_MAGIC_POWER = 20
    BASE_ATTACK_DEFENSE = 2
    BASE_MAGIC_DEFENSE = 10
    BASE_SPEED = 10
    BASE_LUCK = 2
    FEATURES = [
        "It has high magic-power",
        "It doesn't have good attack-power and defense",
        "It works to enemy which has high attack-defense"
    ]
    
    LEVEL_UP_RANGE = {
        "hp" : {"min":3, "max":5, "chance":100},
        "mp" : {"min":3, "max":5, "chance":100},
        "attack_power" : {"min":0, "max":2, "chance":100},
        "magic_power" : {"min":3, "max":5, "chance":100},
        "attack_defense" : {"min":0, "max":2, "chance":100},
        "magic_defense" : {"min":2, "max":4, "chance":100},
        "speed" : {"min":1, "max":1, "chance":50},
        "luck" : {"min":1, "max":1, "chance":20},
    }
    
    SKILL_ACQUISITION = {
        0: [FireBall],
        3: [DoubleFireBall],
        7: [TripleFireBall, Heal],
        10: [IceShard],
        12: [FireBallRain, MegaHeal],
        18: [Inferno]
    }


class Healer(BaseJob):
    BASE_HP = 35
    BASE_MP = 30
    BASE_ATTACK_POWER = 5
    BASE_MAGIC_POWER = 15
    BASE_ATTACK_DEFENSE = 8
    BASE_MAGIC_DEFENSE = 8
    BASE_SPEED = 10
    BASE_LUCK = 7
    FEATURES = [
        "It can heal party member",
        "It wouldn't have good damage skill",
        "It can use easy magic skill"
    ]
    
    LEVEL_UP_RANGE = {
        "hp" : {"min":2, "max":4, "chance":100},
        "mp" : {"min":3, "max":5, "chance":100},
        "attack_power" : {"min":0, "max":1, "chance":100},
        "magic_power" : {"min":2, "max":5, "chance":100},
        "attack_defense" : {"min":0, "max":2, "chance":100},
        "magic_defense" : {"min":2, "max":3, "chance":100},
        "speed" : {"min":1, "max":1, "chance":50},
        "luck" : {"min":1, "max":1, "chance":40},
    }
    
    SKILL_ACQUISITION = {
        0: [Heal, FireBall],
        3: [MegaHeal, IceShard],
        7: [HealAll, GigaHeal],
        10: [DoubleFireBall],
        12: [MegaHealAll],
        18: [GigaHealAll],
    }

class Thief(BaseJob):
    BASE_HP = 40
    BASE_MP = 20
    BASE_ATTACK_POWER = 15
    BASE_MAGIC_POWER = 10
    BASE_ATTACK_DEFENSE = 5
    BASE_MAGIC_DEFENSE = 5
    BASE_SPEED = 15
    BASE_LUCK = 5
    FEATURES = [
        "It can take action twice in a turn",
        "It has a good speed",
        "It can use unique skill to make enemy weak"
    ]
    
    LEVEL_UP_RANGE = {
        "hp" : {"min":3, "max":6, "chance":100},
        "mp" : {"min":2, "max":4, "chance":100},
        "attack_power" : {"min":2, "max":4, "chance":100},
        "magic_power" : {"min":0, "max":2, "chance":100},
        "attack_defense" : {"min":1, "max":3, "chance":100},
        "magic_defense" : {"min":0, "max":1, "chance":100},
        "speed" : {"min":1, "max":1, "chance":100},
        "luck" : {"min":1, "max":1, "chance":30},
    }

    SKILL_ACQUISITION = {
    }

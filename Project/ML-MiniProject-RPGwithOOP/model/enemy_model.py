from model.model import Model
from model import skill_model


class BaseEnemy(Model):
    def __init__(
            self, 
            name: str, 
            hp,
            mp=0,
            attack_power=0,
            magic_power=0,
            attack_defense=0,
            magic_defense=0,
            speed=0,
            luck=0,
            exp=0,
            money=0,
            skills=[]
            ) -> None:
        
        super().__init__(name)
        
        # status
        self.hp = hp
        self.mp = mp
        self.attack_power = attack_power
        self.magic_power = magic_power
        self.attack_defense = attack_defense
        self.magic_defense = magic_defense
        self.speed = speed
        self.luck = luck
        
        # battle status
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
        
        # enemy drop
        self.exp = exp
        self.money = money
        
        # add skills
        self.skills = [skill_model.Attack]
        for skill in skills:
            skill_class = getattr(skill_model, skill)
            self.skills.append(skill_class)
        
class NormalEnemy(BaseEnemy):
    pass

class BossEnemy(BaseEnemy):
    def __init__(self) -> None:
        self.name = "DAEMON(Boss)"
        
        self.hp = 700
        self.mp = 200
        self.attack_power = 50
        self.magic_power = 50
        self.attack_defense = 30
        self.magic_defense = 30
        self.speed = 10
        self.luck = 10
        
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
        
        self.skills = [
            skill_model.Attack,
            skill_model.ShadowStrike,
            skill_model.MegaHeal,
            skill_model.TripleFireBall,
            skill_model.DarkPulse,
            skill_model.Inferno
        ]
from model.job_model import BaseJob


class PartyController:
    def __init__(self) -> None:
        self.party = []
        self.money = 0

    def add_money(self, money:int) -> None:
        self.money += money
        
    def deduct_money(self, money:int) -> None:
        self.money -= money
        if self.money < 0:
            self.money = 0

    def add_character(self, job_instance:BaseJob):
        self.party.append(job_instance)
    
    def reset_current_status(self):
        for character in self.party:
            character.c_hp = character.hp
            character.c_mp = character.mp
            character.c_attack_power = character.attack_power
            character.c_magic_power = character.magic_power
            character.c_attack_defense = character.attack_defense
            character.c_magic_defense = character.magic_defense
            character.c_speed = character.speed
            character.c_luck = character.luck
    
    def party_information(self) -> dict:
        character_infos = list()
        for character in self.party:
            character_infos.append(character.get_status())
        return character_infos
from random import randint, uniform, choice
import json

from controller.user_controller import UserController
from view.battle_view import BattleView
from model import skill_model, enemy_model


class Iterator(object):
    def __init__(self, list_instance):
        self.list_instance = list_instance
        self.value = self.list_instance[0]
        self.i = 0
  
    def next(self):
        if self.i == len(self.list_instance):
            raise StopIteration()
        self.i += 1
        self.value = self.list_instance[self.i]

    def back(self):
        if self.i == 0:
            raise StopIteration()
        self.i -= 1
        self.value = self.list_instance[self.i]
    
    def has_next(self):
        return self.i < len(self.list_instance)-1
    
    def has_back(self):
        return self.i > 0


class BattleController:
    DIFFICULTY_FINE = {
        1: 20,
        2: 30,
        3: 50,
        4: 70,
        5: 100,
    }
    with open("enemy.json", "r") as f:
        enemy:dict = json.load(f)
    
    with open("enemy_party.json", "r") as f:
        enemy_party:list = json.load(f)
        
    NUM_AND_ALPHABET = {
        0: "A", 1: "B", 2: "C", 3: "D", 4: "E",
    }
    
    def __init__(self, party_controller, difficulty:int) -> None:
        self.party_controller = party_controller
        self.battle_view = BattleView()
        self.user_controller = UserController()
        self.fine = self.DIFFICULTY_FINE[difficulty]
        self.enemy_party = self.enemy_generator(difficulty)
        self._action_queue = list()
    
    def generate_boss(self):
        boss = enemy_model.BossEnemy()
        self.enemy_party = [boss]
        self.fine = 200
    
    def enemy_generator(self, difficulty:int) -> list:
        enemy_party = list()
        
        filtered_enemy_party = list(filter(lambda x: x["difficulty"] == difficulty, self.enemy_party))
        choice_enemy = choice(filtered_enemy_party)["enemies"]
        
        for enemy in choice_enemy:
            if enemy["amount"] > 1:
                for i in range(enemy["amount"]):
                    enemy_party.append(enemy_model.NormalEnemy(
                        name=enemy["enemy"] + " " + self.NUM_AND_ALPHABET[i],
                        **self.enemy[enemy["enemy"]]
                        ))
            else:
                enemy_party.append(enemy_model.NormalEnemy(
                        name=enemy["enemy"],
                        **self.enemy[enemy["enemy"]]
                        ))
                
        return enemy_party
    
    def add_action_queue(self, character, action, target=None) -> None:
        self._action_queue.append((character, action, target))
        
    def battle_menu(self) -> bool:
        def skill_target_select(skill) -> list:
            targets = list()
            
            # select itself or entire party or enemy
            if skill.target_type == "itself":
                return [character]
            
            # select 1 or more target
            if skill.target_type == "enemy":
                if skill.target_num == 99:
                    return self.enemy_party
                func = self.select_enemy
                
            elif skill.target_type == "party":
                if skill.target_num == 99:
                    return self.party_controller.party
                func = self.select_party_member
                
            itr = Iterator(range(skill.target_num))
            while True:
                target = func()
                if target == 0 and not itr.has_back():
                    return list()
                elif target == 0:
                    itr.back()
                    targets.pop(-1)
                    continue
                
                targets.append(target)
                if itr.has_next():
                    itr.next()
                else:
                    break

            return targets

        can_continue = True
        while can_continue:
            # show enemies and party status
            self.battle_view.show_enemies(self.enemy_party)
            self.battle_view.show_party(self.party_controller.party)
            
            # show action menu
            for character in self.party_controller.party:
                if character.c_hp == 0:
                    continue
                
                while True:
                    targets = list()
                    self.battle_view.show_action_menu(character)
                    match self.user_controller.int_input(1, 3):
                        case 1:
                            action = skill_model.Attack
                            if (target:=self.select_enemy()) == 0:
                                continue
                            targets.append(target)
                            break
                        case 2:
                            action = skill_model.Block
                            targets.append(character)
                            break
                        case 3:
                            if (action:=self.select_skill(character)) == 0:
                                continue
                            action = character.skills[action-1]
                            if not (targets:=skill_target_select(action)):
                                continue
                            break

                self.add_action_queue(character, action, targets)
            can_continue = self.start_action()
        return self.finish_battle()
    
    def select_skill(self, character) -> int:
        self.battle_view.show_skill(character)
        if (num:=self.user_controller.int_input(0, len(character.skills))) == 0:
            return 0
        
        # make sure character has enough hp and mp to use the skill
        skill_class = character.skills[num-1]
        if (character.c_mp >= skill_class.mp) and (character.c_hp > skill_class.hp):
            return num
        else:
            self.battle_view.show_fail_to_select_skill(character)
            return 0
    
    def select_party_member(self):
        selectable_party_member = list(filter(lambda x: x.c_hp > 0, self.party_controller.party))
        
        self.battle_view.show_party_member_with_number(selectable_party_member)
        num = self.user_controller.int_input(0, len(selectable_party_member))
        if not num:
            return 0
        return selectable_party_member[num-1]

    def select_enemy(self):
        selectable_enemy_party = list(filter(lambda x: x.c_hp > 0, self.enemy_party))
        
        self.battle_view.show_enemy_with_number(selectable_enemy_party)
        num = self.user_controller.int_input(0, len(selectable_enemy_party))
        if not num:
            return 0
        return selectable_enemy_party[num-1]

    def enemy_action_generator(self):
        actable_enemies = list(filter(lambda x: x.c_hp > 0, self.enemy_party))
        actable_party = list(filter(lambda x: x.c_hp > 0, self.party_controller.party))
        for enemy in actable_enemies:
            while True:
                # make list of actable skills
                actable_skills = list()
                for skill in enemy.skills:
                    if (enemy.c_mp >= skill.mp) and (enemy.c_hp > skill.hp):
                        actable_skills.append(skill)
                skill = choice(actable_skills)
                        
                # select target
                targets = list()
                if skill.target_type == 'itself':
                    targets = [enemy]
                elif skill.target_type == 'party':
                    if skill.target_num == 99:
                        targets = self.enemy_party
                    else:
                        for _ in range(skill.target_num):
                            targets.append(choice(actable_enemies))
                elif skill.target_type == 'enemy':
                    if skill.target_num == 99:
                        targets = self.party_controller.party
                    else:
                        for _ in range(skill.target_num):
                            targets.append(choice(actable_party))
                
                # If it is heal, make sure target's hp is not full
                if skill.skill_type == "buff" and skill.affect_to == "hp":
                    if list(filter(lambda x: x.c_hp==x.hp, targets)):
                        continue
                break
            self.add_action_queue(enemy, skill, targets)

    def start_action(self) -> bool:
        def check_can_continue():
            sum_hp = sum([character.c_hp for character in self.party_controller.party])
            if not sum_hp:
                return False
                
            sum_hp = sum([enemy.c_hp for enemy in self.enemy_party])
            if not sum_hp:
                return False
            return True
        
        self.enemy_action_generator()
        while self._action_queue:
            self._action_queue.sort(key=lambda x: x[0].speed, reverse=True)
            character, action, targets = self._action_queue.pop(0)
            
            # make sure character is alive
            if character.c_hp == 0:
                continue
            
            # make sure character has enough hp and mp to do action
            if ((character.c_hp <= action.hp) or (character.c_mp < action.mp)):
                self.battle_view.show_fail_to_do_skill(character, action)
                action = skill_model.Attack
            
            # deduct hp or mp
            character.c_hp -= action.hp
            character.c_mp -= action.mp
            
            attack_formula:str = action.formula
            attack_formula = attack_formula.replace('attack_power', str(character.c_attack_power))
            attack_formula = attack_formula.replace('magic_power', str(character.c_magic_power))
            attack_formula = attack_formula.replace('attack_defense', str(character.c_attack_defense))
            attack_formula = attack_formula.replace('magic_defense', str(character.c_magic_defense))
            attack_damage = eval(attack_formula)
            
            damages = list()
            for target in targets:
                _attack_damage = attack_damage
                # make sure target is alive
                if target.c_hp == 0:
                    # if skill is aoe, skip target
                    if action.target_num == 99:
                        continue
                    
                    # if skill is single target or multi target, change target
                    target=choice(list(filter(lambda x: x.c_hp > 0, self.enemy_party)))
                
                # calculate attack power and defense power
                if (defense_formula:=action.defense_formula):
                    defense_formula = defense_formula.replace('attack_defense', str(target.c_attack_defense))
                    defense_formula = defense_formula.replace('magic_defense', str(target.c_magic_defense))
                    defense_power = eval(defense_formula)
                else:
                    defense_power = 0
                
                critical = False
                if action.skill_type == "attack":
                    # calculate random attack damage
                    _attack_damage = uniform(-0.1, 0.1) * attack_damage + attack_damage
                    
                    # calculate critical
                    if randint(1, 100) < target.c_luck:
                        _attack_damage *= 2
                        critical = True
                
                # calculate damage
                damage = int(_attack_damage - defense_power)
                if (action.skill_type == "attack") and (damage < 0):
                    damage = 0
                
                # affect to target
                current_value = getattr(target, "c_"+action.affect_to)
                if action.skill_type == "buff":
                    setattr(target, "c_"+action.affect_to, (current_value + damage))
                    target.buff_buffer.append({
                        "affect_to": action.affect_to,
                        "value": damage,
                        "count": action.buff_duration
                    })
                else:
                    setattr(target, "c_"+action.affect_to, (current_value - damage))
                
                # make sure hp is not minus
                if getattr(target, "c_hp") < 0:
                    setattr(target, "c_hp", 0)
                damages.append(damage)
                
                if not check_can_continue():
                    break
            
            # show action message
            self.battle_view.show_action_message(
                character, action, targets, int(sum(damages)/len(damages)), critical)
            
            # update queue
            for character, action, targets in self._action_queue:
                if character.c_hp == 0:
                    self._action_queue.remove((character, action, targets))
            
            self.user_controller.input_enter()
            if not check_can_continue():
                return False
            
        self.handle_buff_buffer()
        return True

    def handle_buff_buffer(self):
        for character in self.party_controller.party:
            for buff in character.buff_buffer:
                buff["count"] -= 1
                if buff["count"] == 0:
                    current_value = getattr(character, "c_"+buff["affect_to"])
                    setattr(character, "c_"+buff["affect_to"], (current_value - buff["value"]))
                    character.buff_buffer.remove(buff)
        
        for enemy in self.enemy_party:
            for buff in enemy.buff_buffer:
                buff["count"] -= 1
                if buff["count"] == 0:
                    current_value = getattr(enemy, "c_"+buff["affect_to"])
                    setattr(enemy, "c_"+buff["affect_to"], (current_value - buff["value"]))
                    enemy.buff_buffer.remove(buff)

    def finish_battle(self):
        # lose battle
        party_hp = sum([character.c_hp for character in self.party_controller.party])
        if not party_hp:
            self.party_controller.deduct_money(self.fine)
            self.battle_view.show_lose_message(self.fine)
            self.user_controller.input_enter()
            return False
        
        # calculate exp and money
        exp = sum([enemy.exp for enemy in self.enemy_party])
        money = sum([enemy.money for enemy in self.enemy_party])
        self.battle_view.show_win_message(exp, money)
        
        self.party_controller.add_money(money)
        for character in self.party_controller.party:
            before, after, skills = character.get_exp(exp)
            if before["Level"] != after["Level"]:
                self.battle_view.show_level_up_message(before, after, skills)
        self.user_controller.input_enter()
        return True
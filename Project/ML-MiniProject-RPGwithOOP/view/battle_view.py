from model.job_model import BaseJob


class BattleView:
    def __init__(self) -> None:
        self.battle_count = 0
    
    def show_enemies(self, enemies:list):
        print("\n=========== Battle menu ===========")
        if self.battle_count == 0:
            print("\nYou encountered these enemies!!!")
        else:
            print("\nEnemies status")
            
        for enemy in enemies:
            print("-", enemy.name.ljust(10), f"{enemy.c_hp}/{enemy.hp}")
    
    def show_party(self, party:list):
        print("\nYour current party member status")
        for character in party:
            print(f"- {character.name}({character.__class__.__name__} lv.{character.level})", end="")
            print(f"\tHP:{character.c_hp}/{character.hp} MP:{character.c_mp}/{character.mp}")
    
    def show_action_menu(self, character:BaseJob):
        print(f"\nWhat do you want {character.name} to do?")
        print("1. Attack  2. Block  3. Skill")
    
    def show_skill(self, character:BaseJob):
        print("\n0. Back")
        print("----------------------")
        print(f"{character.name}'s skills")
        for i, skill in enumerate(character.skills):
            print(f"{i+1}. {skill.name}\t{skill.mp}MP {skill.hp}HP")
    
    def show_fail_to_select_skill(self, character):
        print(f"{character.name} don't have enough HP or MP to use this skill")
    
    def show_fail_to_do_skill(self, character, skill):
        print(f"{character.name} don't have enough HP or MP to use {skill.name}")
    
    def show_party_member_with_number(self, party:list):
        print("\nYou can select party member")
        print("0. Back")
        print("--------------------")
        print("PARTY MEMBERS")
        for i, member in enumerate(party):
            print(f"{i+1}. {member.name}")
    
    def show_enemy_with_number(self, enemies:list):
        print("\nYou can select enemy")
        print("0. Back")
        print("--------------------")
        print("ENEMIES")
        for i, enemy in enumerate(enemies):
            print(f"{i+1}. {enemy.name}")
    
    def show_action_message(self, character, action, targets, damage, critical):
        if len(targets) == 1:
            target = targets[0].name
        elif targets[0].__class__.__bases__[0].__name__ == "BaseJob":
            target = "Party members"
        else:
            target = "Enemies"
        
        print(f"\n{character.name} used \"{action.name}\" to {target}!")
        if critical:
            print("Critical Hit!!!", end="")
        
        print("...", end="")
        if action.skill_type == "buff":
            if action.affect_to == "hp":
                print(f"{character.name} got {damage} Heal!")
            else:
                print(f"{character.name} got {action.affect_to} buff!")
            return
    
        if action.skill_type == "debuff":
            print(f"{target} got {action.affect_to} debuff!")
            return
               
        # if it is attack 
        if len(targets) == 1:
            if damage == 0:
                print(f"{target} blocked damage!")
            else:
                print(f"{target} got {damage} damage!")
        else:
            print(f"{target} got {damage} damage as average!")
            
    def show_lose_message(self, fine):
        print("\nYou lose...")
        print(f"You have to pay {fine} money to resurrection")
    
    def show_win_message(self, exp, money):
        print("\nYou slayed enemies!!!")
        print(f"...Your party got {exp} exp!")
        print(f"...You got {money} money!")
    
    def show_level_up_message(self, before, after, new_skills):
        name = before['Name']
        print(f"\n{name} turned into lv.{after['Level']}!")
        del before['Name'], after['Name'], before['Level'], after['Level']
        
        for i, ((b_k, b_v), a_v) in enumerate(zip(before.items(), after.values())):
            b_v, a_v = str(b_v), str(a_v)
            print(b_k.ljust(15), f":{b_v}".ljust(3), "->", a_v.ljust(3), end="")
            if i%2 == 0:
                print("\t", end="")
            else:
                print()
        
        if new_skills:
            print(f"\n{name} come up with new skills!")
            for skill in new_skills:
                print(f"- {skill.name}")
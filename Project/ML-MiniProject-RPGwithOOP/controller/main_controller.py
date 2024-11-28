import random

from controller.user_controller import UserController
from controller.party_controller import PartyController
from controller.battle_controller import BattleController
from view.main_view import MainView
from model.job_model import BaseJob

from names import get_first_name


class MainController:
    def __init__(self):
        self.user_controller = UserController()
        self.party_controller = PartyController()
        self.main_view = MainView()
        self.normal_enemy_count = 0
        self.boss_count = 0
    
    def start_menu(self):
        while True:
            self.main_view.show_start_menu()
            match self.user_controller.int_input(1, 2):
                case 1:
                    self.start_game()
                case 2:
                    return
                
    def start_game(self):
        self.main_view.show_start_game()
        name = self.user_controller.str_input().capitalize()
        
        # Select job class
        while True:
            job_classes = BaseJob.__subclasses__()
            self.main_view.show_create_character(job_classes)
            
            job = self.user_controller.int_input(1, len(job_classes))
            job_class = job_classes[job-1]
            self.main_view.show_job_detail(job_class)
            if self.user_controller.yes_no_input() == 'yes':
                break
        
        # Create instance of selected job class
        job_instance = job_class(name)
        self.party_controller.add_character(job_instance)
        self.main_view.show_navigation()
        self.main_menu()
        
    def party_status(self):
        self.main_view.show_party_status(
            self.party_controller.party,
            self.party_controller.money,
            self.normal_enemy_count,
            self.boss_count
        )
        self.user_controller.input_enter()
    
    def update_hiring(self):
        current_average_level = sum([character.level for character in self.party_controller.party]) // len(self.party_controller.party)
        min_level = current_average_level - 2
        max_level = current_average_level + 5
        if min_level < 1:
            min_level = 1
        if max_level > 40:
            max_level = 40
        
        self.hiring = list()
        for _ in range(4):
            name = get_first_name()
            job_class = random.choice(BaseJob.__subclasses__())
            level = random.randint(min_level, max_level)
            new_person = job_class(name)
            new_person.get_exp(new_person.NEED_EXP_TO_LEVEL_UP[level-1])
            self.hiring.append(new_person)
    
    def hire_member(self):
        self.main_view.show_hiring(self.hiring)
        if (num:=self.user_controller.int_input(0, 4))==0:
            return
        
        hired_person = self.hiring[num-1]
        if self.party_controller.money < hired_person.level*10:
            self.main_view.show_not_enough_money()
            return
        
        self.hiring.remove(hired_person)
        self.party_controller.add_character(hired_person)
        self.party_controller.deduct_money(hired_person.level*10)
        self.main_view.join_party(hired_person.name)
        
        if len(self.party_controller.party) == 5:
            self.remove_member()
            
    def remove_member(self):
        self.main_view.show_remove_member(self.party_controller.party)
        num = self.user_controller.int_input(1, 5)
        removed_person = self.party_controller.party.pop(num-1)
        self.main_view.left_party(removed_person.name)
    
    def boss_battle(self):
        self.main_view.show_boss_battle_description()
        self.user_controller.input_enter()
        if not BattleController(self.party_controller, 3).battle_menu():
            return False
        if not BattleController(self.party_controller, 4).battle_menu():
            return False
        if not BattleController(self.party_controller, 5).battle_menu():
            return False
        boss_battle = BattleController(self.party_controller, 1)
        boss_battle.generate_boss()
        return boss_battle.battle_menu()
    
    def main_menu(self):
        self.update_hiring()
        while True:
            self.party_controller.reset_current_status()
            self.main_view.main_menu()
            match self.user_controller.int_input(1, 4):
                case 1:
                    self.main_view.start_battle()
                    if (difficulty := self.user_controller.int_input(0, 5)) != 0:
                        BattleController(self.party_controller, difficulty).battle_menu()
                        self.normal_enemy_count += 1
                    self.update_hiring()
                case 2:
                    self.party_status()
                case 3:
                    self.hire_member()
                case 4:
                    self.boss_count += 1
                    if self.boss_battle():
                        self.main_view.show_game_clear()
                        self.user_controller.input_enter()
                        break
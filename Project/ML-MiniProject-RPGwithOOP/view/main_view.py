from view.view import View


class MainView(View):
    def show_start_menu(self):
        print("Welcome to RPG game!\n")
        print("You can choose one option:")
        print("1. Start game")
        print("2. Exit")
    
    def show_start_game(self):
        print("\nLet's start your new journey!!!")
        print("What is your name?")
    
    def show_create_character(self, job_classes):
        print("\nWhich job do you want to be?")
        for i, job_class in enumerate(job_classes):
            print(f"{i+1}. {job_class.__name__}")
        
    def show_job_detail(self, job_class):
        print("Job:", job_class.__name__)
        
        print("\nParameter:")
        for i, (k, v) in enumerate(job_class.first_status().items()):
            print(k.ljust(15), f":{v}", end="")
            if i%2 == 0:
                print("\t", end="")
            else:
                print()
        
        print("\nFeatures:")
        for feature in job_class.FEATURES:
            print(" - ", feature)
        
        print(f"\nAre you sure you want to be a {job_class.__name__}? (yes/no)")
        
    def show_navigation(self):
        print("\nNow, it is time to start your new journey...")
        print("Your goal is defeating boss!")
        print("- You can challenge boss anytime")
        print("- But if you died, you must pay money to resurrection")
        print("\nIf you feel not enough to challenge boss")
        print("- You can battle with normal enemies")
        print("- You can hire new member")
        
    def main_menu(self):
        print('\n\n=========== Main menu ===========')
        print("1. Battle with normal enemy")
        print("2. Check party status")
        print("3. Find new party member")
        print("4. Challenge BOSS!")

    def start_battle(self):
        print("0. Back to the menu")
        print("----------------------")
        print("Which enemy do you want to battle?")
        print("1. Level 1")
        print("2. Level 2")
        print("3. Level 3")
        print("4. Level 4")
        print("5. Level 5")    
    
    def show_party_status(self, party, money, normal_count, boss_count):
        print("\n======= Your party status =======")
        for i, character in enumerate(party):
            print(f"{i+1}. {character.name} ({character.__class__.__name__})\tlv.{character.level}")
        
        print("-------------------------")
        print("Money:", money)
        print("Normal enemy count:", normal_count)
        print("Boss count:", boss_count)
      
    def show_hiring(self, hiring):
        print("0. Back to main menu")
        print("============= Hiring! =============  ")
        for i, character in enumerate(hiring, 1):
            print(f"{i}. {character.name} \t{character.__class__.__name__}\tlv.{character.level}", end="")
            print(f"\t-\t{character.level*10} money", )
          
    def show_not_enough_money(self):
        print("\nYou don't have enough money to hire this member")
    
    def join_party(self, name):
        print(f"\n{name} joined your party!")
    
    def show_remove_member(self, party):
        print("You have 5 members in your party")
        print("Which member do you want to remove?")
        for i, character in enumerate(party, 1):
            print(f"{i}. {character.name} ({character.__class__.__name__})\tlv.{character.level}")
    
    def left_party(self, name):
        print(f"\n{name} left your party...")
    
    def show_boss_battle_description(self):
        print("\n============= BOSS challenge =============")
        print("You are about to start boss challenge")
        print("- Before battle with BOSS, You have to defeat 3 normal enemies in a row")
        print("- There is no heal after battle")
        print("- If you died, you have to pay money")
    
    def show_game_clear(self, party, normal_enemy_count, boss_count):
        print("\nCONGRATULATIONS!!! You defeat BOSS!!!")
        print("-------------------------------------")
        print("Your party")
        for character in party:
            print(f"{character.name} ({character.__class__.__name__})\tlv.{character.level}")
        print("-------------------------------------")
        print("Normal enemy count\t:", normal_enemy_count)
        print("Boss count\t\t:", boss_count)
        print("-------------------------------------")
        print("Thank you for playing this game!!!")
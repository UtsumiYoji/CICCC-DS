class UserController:
    def clear_line(self, lines=1):
        for _ in range(lines):
            print("\033[A" + " " * 30 + "\r", end="", flush=True)
        
    def int_input(self, range_low:int=None, range_high:int=None):
        while True:
            try:
                user_input = int(input('>>> '))
                if range_low is not None and (user_input < range_low):
                    pass                    
                elif range_high is not None and (user_input > range_high):
                    pass
                else:
                    return user_input
            except ValueError:
                pass
            
            self.clear_line()
    
    def str_input(self):
        while True:
            user_input = input('>>> ')
            if user_input:
                return user_input
            self.clear_line()
            
    def yes_no_input(self):
        while True:
            user_input = input('>>> ')
            if user_input.lower() in ['yes', 'no']:
                return user_input
            self.clear_line()
    
    def input_enter(self):
        input('>>> (Press enter to continue...)')
        self.clear_line()
# Problem 1
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def car_infor(self):
        return f"Car: {self.make} {self.model} {self.year}"

car_instance = Car("Toyota", "Corolla", 2020)
print(car_instance.car_infor())


# Problem 2
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

rectangle_instance = Rectangle(5, 10)
print(rectangle_instance.get_area())
print(rectangle_instance.get_perimeter())


# Problem 3
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            return "Insufficient funds"

    def get_balance(self):
        return self.__balance
    
account_instance = Account(98765432, 1000)
account_instance.deposit(300)
account_instance.withdraw(500)
print(account_instance.get_balance())


# Problem 4
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"
    
person_instance = Person("John", 30)
print(person_instance)


# Problem 5
class Team:
    def __init__(self, members:list=[]):
        self.members = members

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        self.members.remove(member)
    
    def get_member(self):
        return self.members

team_instance = Team()
team_instance.add_member("Alice")
team_instance.add_member("Bob")
team_instance.add_member("Charlie")
team_instance.remove_member("Bob")
print(team_instance.get_member())


# Problem 6
class Bank:
    def __init__(self, name, account:list=[]):
        self.name = name
        self.account = account

    def add_account(self, account:int):
        self.account.append(account)

    def remove_account(self, account:int):
        self.account.remove(account)
    
    def get_account(self):
        return self.account
    
    def bank_info(self):
        return f"Bank: {self.name}, Account: {len(self.account)}"

bank_instance = Bank("Bank of Python")
bank_instance.add_account(1111)
bank_instance.add_account(2222)
bank_instance.add_account(3333)
bank_instance.remove_account(2222)
print(bank_instance.bank_info())


# Problem 7
class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
    
    def check_paaaword(self, password):
        return self.password == password
    
user_instance = User("user1", "pass123")
print(user_instance.check_paaaword("pass123"))


# Problem 8
class Employee:
    def __init__(self, name, position, salary=50000) -> None:
        self.name = name
        self.position = position
        self.salary = salary
    
    def emoployee_info(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}"

employee_instance = Employee("Jane", "Developer")
print(employee_instance.emoployee_info())


# Problem 9
class MathOperation:
    @staticmethod
    def add(x, y):
        return x + y
    
print(MathOperation.add(10, 20))


# Problem 10
class Counter:
    count = 0

    def __init__(self) -> None:
        Counter.count += 1
    
    @staticmethod
    def get_count():
        return Counter.count

Counter(), Counter(), Counter()
print(Counter.get_count())
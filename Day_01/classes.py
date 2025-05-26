
# 1. Classes
# Classes are blueprints for creating objects. They encapsulate data (attributes) and behavior (methods) together.
# Basic Class Definition
"""class Dog:
    pass
my_dog = Dog()
print(type(my_dog))"""

# Class with Attributes and Methods
"""class Car:
    wheels = 4

    def start_engine(self):
        print("Engine started")
    def stop_engine(self):
        print("Engine stopped")

car1 = Car()
car2 = Car()

print(car1.wheels)
print(car2.wheels)

car1.start_engine()
car2.stop_engine()"""

# 2.2. The __init__ Constructor
# The __init__ method is automatically called when creating a new instance. It initializes the object's attributes.
# Basic Constructor
"""class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age}  years old")
person1 = Person("Sreenu",23)
person2 = Person("Pandu",19)
person1.introduce()
person2.introduce()"""

# Constructor with Default Values
"""class BankAccount:
    def __init__(self,acc_holder,intial_bal=0):
        self.acc_holder = acc_holder
        self.balance = intial_bal
        self.transaction_history = []

    def deposite(self,amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")
        print(f"Deposited ${amount}.New balance: {self.balance}")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"withdraw ${amount}")
            print(f"withdraw ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")
    def get_balance(self):
        return self.balance
    
account1 = BankAccount("Srinu")
account2 = BankAccount("Pandu",1000)

account1.deposite(500)
account2.withdraw(200)"""
        

# 3. The self Keyword
# self refers to the current instance of the class. It's used to access instance attributes and methods.
# Understanding self
"""class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        self.subjects = []
    def add_subject(self,subject):
        self.subjects.append(subject)
        print(f"{self.name} added {subject}")
    
    def display_info(self):
        print(f"Student: {self.name}")
        print(f"Grade: {self.grade}")
        print(f"Subjects: {','.join(self.subjects)}")
student1 = Student("Srinu",10)
student2 = Student("Pandu",11)

student1.add_subject("Math")
student2.add_subject("Science")

student1.display_info()
student2.display_info()"""

# self in Method Calls
"""class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, number):
        self.result += number
        return self  
    
    def multiply(self, number):
        self.result *= number
        return self
    
    def get_result(self):
        return self.result
    
    def reset(self):
        self.result = 0
        return self

calc = Calculator()
result = calc.add(5).multiply(3).add(2).get_result()
print(result)  """


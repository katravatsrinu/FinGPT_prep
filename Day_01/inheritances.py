# 4. Inheritance
# Inheritance allows a class to inherit attributes and methods from another class.
# Basic Inheritance

# Parent class (Base class)
"""class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    
    def make_sound(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Canine")  
        self.breed = breed
    
    def make_sound(self):  
        print(f"{self.name} barks: Woof!")
    
    def fetch(self):  
        print(f"{self.name} is fetching the ball")

class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name, "Feline")
        self.indoor = indoor
    
    def make_sound(self):  
        print(f"{self.name} meows: Meow!")
    
    def climb(self):  
        print(f"{self.name} is climbing")


dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", indoor=True)

dog.eat()    
cat.sleep()  

dog.make_sound()  
cat.make_sound()  

dog.fetch()  
cat.climb()  

print(f"{dog.name} is a {dog.breed} {dog.species}") 
print(isinstance(dog, Dog))     
print(isinstance(dog, Animal))  
print(isinstance(dog, Cat))     

print(issubclass(Dog, Animal))  
print(issubclass(Cat, Animal))  
print(issubclass(Dog, Cat))"""

# Multiple Inheritance
"""class Swimmer:
    def swim(self):
        print("Swimming gracefully")

class Flyer:
    def fly(self):
        print("Flying through the air")

class Duck(Animal, Swimmer, Flyer):  # Multiple inheritance
    def __init__(self, name):
        super().__init__(name, "Bird")
    
    def make_sound(self):
        print(f"{self.name} quacks: Quack!")

duck = Duck("Donald")
duck.eat()   
duck.swim()  
duck.fly()   
duck.make_sound()"""



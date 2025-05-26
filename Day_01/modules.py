# 6. Modules
# Modules are files containing Python code that can be imported and reused in other programs.
# Importing Standard Modules
# Math Module
import random
import math
import datetime

print(math.pi)                
print(math.sqrt(16))          
print(math.ceil(4.2))         
print(math.floor(4.8))        
print(math.factorial(5))      
print(math.sin(math.pi/2)) 



now = datetime.datetime.now()
print(now)
birthday = datetime.date(2001,11,2)
print(birthday)
today = datetime.date.today()
age_days = today-birthday
print(f"Days old: {age_days.days}")

formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)


# Random numbers
print(random.randint(1, 10))      # Random integer between 1 and 10
print(random.random())            # Random float between 0 and 1
print(random.uniform(1.5, 10.5))  # Random float between 1.5 and 10.5

# Random choices
colors = ["red", "blue", "green", "yellow"]
print(random.choice(colors))      # Random choice from list
print(random.sample(colors, 2))   # Random sample of 2 items

# Shuffling
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # List is shuffled in place
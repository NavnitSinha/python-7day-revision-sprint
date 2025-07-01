## Day 1: Python Core Refresh

---

# Topics:

Variables & Data Types: int, float, str, bool, None
Strings: indexing, slicing, methods (upper(), split(), etc.)
Conditionals: if, elif, else
Loops: for, while, break, continue
range() and enumerate()

---

# Try These Tasks:

Variable Practice:

name = "Navnit"
age = 25
height = 5.9
is_employed = True

String Play:

quote = "Python is powerful!"
print(quote.upper())
print(quote[0:6])
print(quote.split())

Conditionals:

temp = 30
if temp > 35:
    print("Too hot!")
elif temp > 25:
    print("Warm")
else:
    print("Cool")
    
For Loop + Range:

for i in range(5):
    print("Count:", i)
    
While Loop + Break:

n = 0
while True:
    if n == 3:
        break
    print("Looping", n)
    n += 1
    
Enumerate Example:

colors = ["red", "blue", "green"]
for idx, color in enumerate(colors):
    print(f"{idx}: {color}")

- What enumerate() Does:
     Enumerate(colors) turns your list into something like this behind the scenes: [(0, "red"), (1, "blue"), (2, "green")]

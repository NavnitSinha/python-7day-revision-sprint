'''Mini Project: Journal Logger (Text File Edition)

🧠 What It’ll Do:
Ask the user to enter a journal entry
Save it to a .txt file
Show all past entries if user wants to read

✅ Features to Include:
File writing with "a" mode (append)
File reading with "r" mode
try-except block to handle file errors
Maybe show timestamp? (if you're feelin' spicy 🌶)'''

# Writing to file (this will overwrite existing content)
with open("journal.txt", "w") as j:
    j.write("This is my journal\n")
    j.write("I'm Navnit Sinha and I am the greatest of all time.\n")

# Reading the file content
with open("journal.txt", "r") as j:
    content = j.read()
    print("Here's what you wrote:\n", content)

# Appending new content
with open("journal.txt", "a") as j:
    j.write("I am sorry if you feel wrong about this, it is what it is!!!\n") 

# Error-handling block
try: 
    with open("journal.txt", "r") as j: 
        content = j.read() 
        print(content)
except FileNotFoundError:  
    print("File not found! Try again!")

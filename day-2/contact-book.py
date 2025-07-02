'''Day 2 Mini Project: Contact Book
A clean little app using:
✅ Functions (add, search, list contacts)
✅ Lists (to hold contacts)
✅ Dictionaries (each contact is a dict)
📘 Requirements:
Add a contact: name, phone number, email
View all contacts
Search contact by name
'''

def contacts(name, number):
    return f"{name} - {number}"
    
contact = {"Asha": "7823543789", "Neel": "9374783893", "Ritu": "7598437903"}

while True:
    print("Select what you want to do:\n")
    print("1. Add a contact (Add) \n2. View all contacts (View)\n3. Search contact by name (Search) \n4. Quit")
    choice = input("Enter your choice: ")
    if choice.lower() == "Add":
        add_name = input("Enter Name of the person you want to Add: ")
        add_num = int(input("Enter Number of the person you want to Add: "))
        contact[add_name] = add_num
        print(f"{add_name} added to the list")
    elif choice.lower() == "View":
        for name, number in contact.items():
            print(contacts(name, number))
    elif choice.lower() == "Search":
        search = input("Enter the Name of the person you want to search: ")
        if search in contact:
            print(f"Found it! {contacts(name, number)}")
        else:
            print("This name doesn't exist. Please try again.")
    elif choice.lower() == "Quit":
        print("Good Bye! It was pleasure helping you!")
        break
    else:
        print("This option doesn't exist")

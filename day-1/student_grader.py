'''Goal:
Ask user to enter names and scores of 3 students
Store them in a list
Use conditionals to give grades (A/B/C/Fail)
Use enumerate() to display roll numbers'''

students = []
for i in range(4):
    name = input("Enter student name: ")
    scores = int(input("Enter student scores: "))
    students.append((name, scores))

print("📋 Student Report Card: ")
for idx, (name, scores) in enumerate(students, start = 1):
    if scores > 90:
        grade = "A"
    elif scores > 85:
        grade = "B"
    elif scores > 70: 
        grade = "C"
    elif scores > 55: 
        grade = "D"
    else: 
        grade = "FAILED"
        
    print(f"{idx}: {name} scored {scores}  →  Grade: {grade}")



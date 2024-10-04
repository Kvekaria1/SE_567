import random

def student_groups(students):
   
    sorted_students = sorted(students, key=lambda student: student[1])

    groups = [[], [], []]
    for i, student in enumerate(sorted_students):
        groups[i % 3].append(student)  
    
    for group in groups:
        random.shuffle(group)
    
    
    for i, group in enumerate(groups):
        print(f"Group {i + 1}: {group}")


students = [
    ("Krish", "vekaria"),
    ("Zeel", "desai"),
    ("drashti", "rudani"),
    ("aayush", "gandhi"),
    ("krina", "hirpara"),
    ("soham", "joshi"),
    ("yash", "patel"),
    ("nayan", "patel"),
    ("krrish", "patel")
]


student_groups(students)

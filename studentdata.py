students = {
    101: {"name": "Amit", "marks": [78, 85]},
    102: {"name": "Om", "marks": [90, 91]},
    103: {"name": "Sangam", "marks": [10, 10]}
}

for roll, details in students.items():
    marks = details["marks"]

    first_sub = marks[0]
    second_sub = marks[1]

    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)

    print("\nRoll No:", roll)
    print("Name:", details["name"])
    print("Marks:", marks)
    print("First Subject:", first_sub)
    print("Second Subject:", second_sub)
    print("Total:", total)
    print("Average:", average)
    print("Highest:", highest)
# ==========================================
# DAY 2 ADVANCED+ PROJECT
# STUDENT RESULT MANAGEMENT SYSTEM (SRMS)
# ==========================================

print("STUDENT RESULT MANAGEMENT SYSTEM ===")

# Step 1: Collect number of students
num_students = int(input("Enter number of students: "))

# Step 2: Prepare a data structure (list of dictionaries)
students = []

# Step 3: Input loop for each student
for i in range(num_students):
    print(f"\n--- Enter details for Student {i+1} ---")
    name = input("Enter Student Name: ")

    # Collect subject scores
    math = float(input("Enter Mathematics score: "))
    eng = float(input("Enter English score: "))
    phy = float(input("Enter Physics score: "))
    chem = float(input("Enter Chemistry score: "))
    bio = float(input("Enter Biology score: "))

    # Calculate total and average
    total = math + eng + phy + chem + bio
    avg = round(total / 5, 2)

    # Determine grade
    if avg >= 90:
        grade = "A+"
    elif avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    elif avg >= 50:
        grade = "D"
    else:
        grade = "F"

    # Store data in dictionary
    student = {
        "name": name,
        "math": math,
        "eng": eng,
        "phy": phy,
        "chem": chem,
        "bio": bio,
        "total": total,
        "average": avg,
        "grade": grade
    }

    # Add to list
    students.append(student)

# Step 4: Display report summary
print("\n=== CLASS REPORT ===")
print(f"{'Name':<15}{'Total':<10}{'Average':<10}{'Grade':<6}")
print("-" * 45)

# Track top performer
top_student = students[0]
for s in students:
    print(f"{s['name']:<15}{s['total']:<10}{s['average']:<10}{s['grade']:<6}")
    if s['average'] > top_student['average']:
        top_student = s

# Step 5: Class performance analytics
class_total = sum([s['average'] for s in students])
class_average = round(class_total / num_students, 2)

print("\n=== CLASS SUMMARY ===")
print(f"Class Average: {class_average}")
print(f"Top Student: {top_student['name']} ({top_student['average']}) with Grade {top_student['grade']}")

# Step 6: Optional - Save to file
save = input("\nDo you want to save this report to a file? (yes/no): ").lower()
if save == "yes":
    with open("student_report.txt", "w") as f:
        f.write("STUDENT RESULT MANAGEMENT SYSTEM REPORT\n\n")
        for s in students:
            f.write(f"{s['name']}\n Total: {s['total']}\n Avg: {s['average']}\n1 Grade: {s['grade']}\n")
        f.write(f"\nClass Average: {class_average}\n")
        f.write(f"Top Student: {top_student['name']} ({top_student['average']})\n")
    print("✅ Report successfully saved as 'student_report.txt'")
else:
    print("Report not saved.")

num_students = int(input("Enter the number of students: ")) 
Students = [] 
for i in range(num_students): 
  name = input(f"Enter name of student {i+1}: ") 
  marks = float(input(f"Enter marks of student {i+1}: ")) 
  Students.append((name, marks)) 
total_marks = sum(marks for name, marks in Students) 
average_marks = total_marks / num_students 
print(f"Average marks: {average_marks}") 
print("Students who scored above average:") 
for name, marks in Students: 
  if marks > average_marks: 
    print(f"{name} - {marks}")

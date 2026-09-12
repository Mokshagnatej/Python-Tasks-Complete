employees = [ 
    (101, 'Alice', 'HR'), 
    (102, 'Bob', 'IT'), 
    (103, 'Charlie', 'Finance'), 
    (104, 'David', 'IT'), 
    (105, 'Eva', 'Marketing') 
    ] 
print("Employees from IT Department:")
 for emp in employees: 
 emp_id, name, department = emp 
 if department == 'IT': 
   print(f"ID: {emp_id}, Name: {name}, Department: {department}")

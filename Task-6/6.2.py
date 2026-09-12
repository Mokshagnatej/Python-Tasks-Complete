emp_id = input("Enter employee ID to update: ")
new_salary = input("Enter new salary: ")
lines = []
with open("salary.txt", "r") as f:
    for line in f:
        eid, name, sal = line.strip().split(",")
        if eid == emp_id:
            line = eid + "," + "," + new_salary +"\n"
        lines.append(line)
with open("salary.txt", "w") as f:
    f.writelines(lines)
print("Salary updated successfully.")

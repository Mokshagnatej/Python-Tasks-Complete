with open("attendance.txt", "r") as f: 
for line in f: 
  name, percent = line.strip().split(",") 
  if float(percent) < 76: 
    print(f"{name} has low attendance ({percent})")

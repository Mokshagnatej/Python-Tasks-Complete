marks = [45, 56, 67, 78, 89, 90, 34, 56, 22, 48, 67, 76, 54, 32, 88, 95, 71, 65, 59, 60, 40, 36, 84, 74, 53, 92, 66, 81, 19, 70]
 search_mark = int(input("Enter mark to search: "))
 found = False 
for i in range(len(marks)): 
 if marks[i] == search_mark: 
 print(f"Mark found at position {i + 1}") 
 found = True 
 break 
if not found: 
 print("Mark not found")

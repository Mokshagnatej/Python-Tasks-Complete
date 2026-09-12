print("Select operation:") 

print("1. Add") 

print("2. Subtract")

 print("3. Multiply") 

print("4. Divide") 

choice = input("Enter choice (1/2/3/4): ") 

a = float(input("Enter first number: "))

 b = float(input("Enter second number: ")) 

if choice == '1': 

 print(f"{a} + {b} = {a + b}") 

elif choice == '2': 
 print(f"{a} - {b} = {a - b}") 

elif choice == '3':
     
 print(f"{a} * {b} = {a * b}") 
 
elif choice == '4':     

if b != 0: 

 print(f"{a} / {b} = {a / b}") 

else: 

 print("Error: Division by zero") 

else: 

 print("Invalid choice")


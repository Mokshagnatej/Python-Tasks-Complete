import math 

N = int(input("Enter an integer: "))

 N_plus_1 = N + 1

 sqrt_val = math.isqrt(N_plus_1) 

if sqrt_val * sqrt_val == N_plus_1: 
  print("Yes") 
else: 
 print("No")

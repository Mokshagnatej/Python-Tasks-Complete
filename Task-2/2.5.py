n = int(input("Enter a number: "))

 if n <= 1: 

  print("Not a prime number")

 else:

     is_prime = True 

    i = 2 

    while i < n: 

    if n % i == 0: 

    is_prime = False 

    break 
    i += 1 
    if is_prime: 
     print("Prime number") 
    else: 
    print("Not a prime number")

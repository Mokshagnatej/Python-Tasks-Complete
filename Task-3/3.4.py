N = int(input("Enter a number between 1 and 25000: ")) 
digit_str = str(N) 
digit_count = {} f
or digit in digit_str: 
 digit_count[digit] = digit_count.get(digit, 0) + 1 non_repeated_count = sum(1 for count in digit_count.values() if count == 1) print(non_repeated_count)

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative!")
    elif age < 18:
        print("❌ You are not eligible to vote.")
    else:
        print("✅ You are eligible to vote.")
except ValueError as e:
    print("Invalid input:", e)

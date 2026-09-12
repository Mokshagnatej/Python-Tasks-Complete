
def check_password(password):
    if (len(password) >= 8 and
        any(ch.isupper() for ch in password) and
        any(ch.islower() for ch in password) and
        any(ch.isdigit() for ch in password) and
        any(ch in "!@#$%^&*()" for ch in password)):
        return "Strong"
    else:
        return "Weak"

user_password = input("Enter password to check strength: ")
strength = check_password(user_password)
if strength == "Strong":
    print("Input meets complexity requirements.")
else:
    print("Input does not meet complexity requirements.")

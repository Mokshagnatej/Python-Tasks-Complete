
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
password_strength = check_password(user_password)
print(f"Password strength: {password_strength}")

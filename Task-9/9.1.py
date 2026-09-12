try:
    balance = 5000
    amount = int(input("Enter withdrawal amount: "))

    if amount > balance:
        raise ValueError("Insufficient Balance!")
    else:
        balance -= amount
        print(f"✅ Withdrawal Successful! Remaining Balance: {balance}")
except ValueError as e:
    print("❌ Error:", e)

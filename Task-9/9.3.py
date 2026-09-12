marks = []
try:
    for i in range(5):
        m = int(input(f"Enter marks of student {i+1}: "))
        if m < 0 or m > 100:
            raise ValueError("Marks should be between 0 and 100")
        marks.append(m)

    avg = sum(marks) / len(marks)
    print("✅ Average Marks:", avg)

except ValueError as e:
    print("❌ Error:", e)

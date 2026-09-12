
import matplotlib.pyplot as plt

quarters = ["Q1", "Q2", "Q3", "Q4"]
sales_2023 = [150, 200, 170, 220]
sales_2024 = [180, 210, 190, 250]

x = range(len(quarters))

plt.bar(x, sales_2023, width=0.4, label="2023", color="blue")
plt.bar([i+0.4 for i in x], sales_2024, width=0.4, label="2024", color="green")

plt.xticks([i+0.2 for i in x], quarters)
plt.xlabel("Quarters")
plt.ylabel("Sales (in $1000s)")
plt.title("Quarterly Sales Comparison")
plt.legend()
plt.show()

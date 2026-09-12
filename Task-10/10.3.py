import matplotlib.pyplot as plt

companies = ["Apple", "Samsung", "Xiaomi", "Others"]
market_share = [30, 35, 20, 15]

plt.pie(market_share, labels=companies, autopct="%1.1f%%", startangle=90, shadow=True)
plt.title("Mobile Market Share Distribution")
plt.show()

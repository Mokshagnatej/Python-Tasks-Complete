
import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperature = [28, 30, 32, 31, 29, 27, 26]

plt.plot(days, temperature, marker="o", linestyle="--", color="red")
plt.xlabel("Days of the Week")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Variation Over a Week")
plt.grid(True)
plt.show()

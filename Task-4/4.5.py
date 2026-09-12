inventory = { 
    "Apples": (50, 20), 
    "Bananas": (10, 0), 
    "Oranges": (30, 15), 
    "Grapes": (40, 0), 
    "Mangoes": (60, 12)
  }
 total_value = 0
print("Out of stock items:") 
for item, (price, quantity) in inventory.items(): 
 if quantity == 0: 
  print(f"- {item}") 
 else: 
   total_value += price * quantity
 print(f"Total value of available stock: ${total_value}")

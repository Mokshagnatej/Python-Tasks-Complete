day_1 = ["apple", "banana", "orange", "apple"]
 day_2 = ["banana", "Kiwi", "grape"]
 day_3 = ["orange", "grape", "melon", "apple"]
 all_items = day_1 + day_2 + day_3
 unique_items = set(all_items) 
print("Unique items sold over 3 days:") 
for item in unique_items: 
 print(item)

prices = [1200, 1500, 1000, 2500] 
prices.sort()
 print("Sorted prices:", prices)  
def binary_search(arr, x): 
low, high = 0, len(arr) - 1 
while low <= high: 
mid = (low + high) // 2 
 if arr[mid] == x: 
   return mid 
 elif arr[mid] < x: 
   low = mid + 1 
else: 
  high = mid - 1 
return -1 

 price = int(input("Enter price to search: "))
 pos = binary_search(prices, price) 
if pos != -1: 
  print(f"Price {price} found at position {pos + 1}")
 else: 
  print("Price not found")

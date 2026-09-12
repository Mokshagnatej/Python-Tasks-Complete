patients = [105, 102, 110, 101, 120, 108, 115] 
patients.sort() 
print("Sorted patient IDs:", patients)  
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
  pid = int(input("Enter patient ID to search: "))
 pos = binary_search(patients, pid) 
if pos != -1: 
    print(f"Patient ID found at position {pos + 1}") 
else: 
    print("Patient ID not found")

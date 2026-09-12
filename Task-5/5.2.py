books = ["Python Basics", "Data Structures", "Algorithm", "C Programming", "Database System", "Operating Systems", "Artificial Intelligence"] 
books.sort()
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
 book = input("Enter book title to search: ")
 pos = binary_search(books, book) 
if pos != -1: 
  print(f"Book found at position {pos + 1}")
 else:
  print("Book not found")
 

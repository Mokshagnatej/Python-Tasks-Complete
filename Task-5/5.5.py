scores = [56, 78, 90, 65, 88, 72, 95] 
scores.sort(reverse=True) 
print("Ranking (High to low):", scores) 
 s = int(input("Enter team score to search: ")) i
f s in scores: 
  print(f"Team with score {s} is ranked {scores.index(s) + 1}") 
else: 
  print("Score not found")

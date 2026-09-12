paragraph = "Python is great. Python is easy to learn. Learn Python and be productive."
 word_count = {} 
for word in paragraph.split(): 
  word = word.lower().strip('. ,') 
  if word in word_count: 
     word_count[word] += 1 
  else: 
    word_count[word] = 1 
print("Word frequencies in the paragraph:") 
for word, count in word_count.items(): 
  print(f"{word}: {count}")


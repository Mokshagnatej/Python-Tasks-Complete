def paginate(data, page_size):
    for i in range(0, len(data), page_size):
        yield data[i:i+page_size]

# Example
results = list(range(1, 21))  # 20 results
for page in paginate(results, 5):
    print(page)

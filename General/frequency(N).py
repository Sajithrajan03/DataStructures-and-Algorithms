data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
frequency_distribution = {}
for item in data:
    if item in frequency_distribution:
        frequency_distribution[item] += 1
    else:
        frequency_distribution[item] = 1
sorted_distribution = sorted(frequency_distribution.items(), key=lambda x: x[1], reverse=True)
n = 5
top_n_distribution = sorted_distribution[:n]
for item, frequency in top_n_distribution:
    print(f"Item: {item}, Frequency: {frequency}")

data = [i for i in range(0,10)]
items = set(data)
frequency_distribution = {}
for item in data:
    if item in frequency_distribution:
        frequency_distribution[item] += 1
    else:
        frequency_distribution[item] = 1
    print(frequency_distribution)

for i in items:
    print(f"Item: {i}, Frequency: {frequency_distribution[i]}")
    

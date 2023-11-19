def fair_partition(arr, k):
    def is_feasible(mid):
        count = 1
        current_sum = 0
        partitioned_arr = [[]]

        for num in arr:
            if current_sum + num > mid:
                count += 1
                current_sum = 0
                partitioned_arr.append([])

            current_sum += num
            partitioned_arr[-1].append(num)

        return count <= k, partitioned_arr

    low, high = max(arr), sum(arr)

    while low <= high:
        mid = (low + high) // 2

        feasible, partitioned_arr = is_feasible(mid)

        if feasible:
            high = mid - 1
        else:
            low = mid + 1

    return partitioned_arr

# Test the algorithm and print the partitioned array
arr = [100, 400, 300, 400, 500, 600, 700, 800, 100]
k = 3
result = fair_partition(arr, k)
print("Fair partitioning result:", result)

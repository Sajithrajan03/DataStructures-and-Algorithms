def MaximaSet(S):
    # Base case: If the set S has only one point, return S
    if len(S) == 1:
        return S

    # Find the median point p in S by lexicographic (r)-coordinates
    p_index = len(S) // 2
    p = sorted(S, key=lambda point: (point[0], point[1]))[p_index]

    # Split S into two sets: L and G
    L = [point for point in S if point < p]
    G = [point for point in S if point >= p]

    # Recursively find maxima sets for L and G
    M1 = MaximaSet(L)
    M2 = MaximaSet(G)

    # Find the lexicographically smallest point in M2
    smallest_point_in_M2 = min(M2, key=lambda point: (point[0], point[1]))

    # Remove points from M1 whose y-coordinates are less than y(smallest_point_in_M2)
    M1 = [point for point in M1 if point[1] >= smallest_point_in_M2[1]]

    # Combine the results
    return M1 + M2

 
points = [(1, 1), (2, 5), (3, 3), (5, 8), (6, 6), (7, 7), (8, 2), (9, 4)]
maxima_set = MaximaSet(points)
print("Maxima Set:", maxima_set)

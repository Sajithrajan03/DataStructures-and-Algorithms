import random
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class SnakesAndLadders:
    def __init__(self, size, snakes, ladders, k):
        self.size = size
        self.snakes = snakes
        self.ladders = ladders
        self.k = k
        self.adjacency_list = self.createGraph()

    def createGraph(self):
        adjacency_list = {i: [] for i in range(1, self.size + 1)}
        
        for ladder in self.ladders:
            adjacency_list[ladder[0]].append(ladder[1])
        
        for snake in self.snakes:
            adjacency_list[snake[0]].append(snake[1])
        
        return adjacency_list

    def getNeighbors(self, position):
        if len(self.adjacency_list[position]) > 0:
            return self.adjacency_list[position]
        else:
            neighbors = []
            for neighbor in range(position + 1, min(position + self.k + 1, self.size + 1)):
                neighbors.append(neighbor)
            return neighbors

    def canReachGoal(self):
        visited = [False] * (self.size + 1)
        queue = [1]

        while queue:
            position = queue.pop(0)
            if position == self.size:
                return True
            if not visited[position]:
                visited[position] = True
                queue.extend(self.getNeighbors(position))

        print(f"Goal cannot be reached from 1 to {self.size}")
        return False

    def noSnakeLadderInSameSquare(self):
        occurence = [0] * (self.size + 1)
        
        for i in range(1, self.size + 1):
            if len(self.adjacency_list[i]) > 1:
                return False
            for neighbor in self.adjacency_list[i]:
                occurence[neighbor] += 1
                occurence[i] += 1

        for i in range(1, self.size + 1):
            if occurence[i] > 1:
                print(f"Invalid board. Snake/Ladder found in the same square: {i}")
                return False
            
        return True

    def isCyclicBasedOnTopologicalSort(self):
        graph = nx.DiGraph()
        for i in range(1, self.size + 1):
            for neighbor in self.adjacency_list[i]:
                graph.add_edge(i, neighbor)

        try:
            cycle = list(nx.find_cycle(graph, orientation='original'))
            print(f"Cycle found: {cycle}")
            return True
        except nx.NetworkXNoCycle:
            return False

    def noDirectPathFromStartToEnd(self):
        return self.size not in self.adjacency_list[1]

    def shortestPath(self):
        if not self.canReachGoal() or not self.noSnakeLadderInSameSquare() or not self.noDirectPathFromStartToEnd() or self.isCyclicBasedOnTopologicalSort():
            print("Board is invalid. Cannot find shortest path.")
            return None

        # Find shortest path using BFS
        visited = [False] * (self.size + 1)
        parent = [None] * (self.size + 1)
        queue = [(1, 0)]
        visited[1] = True

        while queue:
            position, distance = queue.pop(0)
            if position == self.size:
                break
            for neighbor in self.getNeighbors(position):
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = position
                    queue.append((neighbor, distance + 1))

        # Backtrack to find the shortest path
        path = []
        position = self.size
        while position != 1:
            path.append(position)
            position = parent[position]
        path.append(1)
        path.reverse()

        return {
            "distance": len(path) - 1,
            "path": path
        }

def plot_histogram(dice_rolls):
    plt.figure(figsize=(8, 6))
    plt.hist(dice_rolls, bins=np.arange(0.5, 7.5, 1), edgecolor='black', alpha=0.7, rwidth=0.85)
    plt.title("Dice Roll Frequencies")
    plt.xlabel("Dice Roll")
    plt.ylabel("Frequency")
    plt.xticks(range(1, 7))
    plt.grid(axis='y', alpha=0.75)
    plt.show()

def plot_shortest_path(size, snakes, ladders, shortest_path):
    G = nx.Graph()
    
    for i in range(1, size + 1):
        G.add_node(i)

    for snake in snakes:
        G.add_edge(snake[0], snake[1], color='red', weight=2)

    for ladder in ladders:
        G.add_edge(ladder[0], ladder[1], color='green', weight=2)

    pos = {i: (i % size, i // size) for i in range(1, size + 1)}
    
    edges = G.edges()
    colors = [G[u][v]['color'] for u, v in edges]
    weights = [G[u][v]['weight'] for u, v in edges]

    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_weight='bold', edge_color=colors, width=weights)
    
    # Highlight the shortest path
    path_edges = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path) - 1)]
    path_colors = ['blue' for _ in path_edges]
    path_weights = [2 for _ in path_edges]
    nx.draw(G, pos, edgelist=path_edges, edge_color=path_colors, width=path_weights, arrows=False)
    
    plt.title("Shortest Path on Snakes and Ladders Board")
    plt.show()

if __name__ == "__main__":
    test_cases = [
        {
            "size": 100,
            "snakes": [(16, 6), (47, 26), (49, 11), (56, 53), (62, 19), (64, 60), (87, 24), (93, 73), (95, 75), (98, 78)],
            "ladders": [(1, 38), (4, 14), (9, 31), (21, 42), (28, 84), (36, 44), (51, 67), (71, 91), (80, 100)],
            "k": 6,
        },
        {
            "size": 100,
            "snakes": [(16, 6), (47, 26), (49, 11), (56, 53), (62, 19), (64, 60), (87, 24), (93, 73), (95, 75), (98, 78), (100, 38)],
            "ladders": [(4, 14), (9, 31), (21, 42), (28, 84), (36, 44), (51, 67), (71, 91)],
            "k": 6,
        },
        {
            "size": 100,
            "snakes": [(16, 6), (47, 26), (49, 11), (56, 53), (62, 19), (64, 60), (87, 24), (93, 73), (100,38), (98, 78)],
            "ladders": [(1, 38), (38, 39), (9, 31), (21, 42), (28, 84), (36, 44), (51, 67), (71, 91), (80, 100)],
            "k": 6,
        },
        {
            "size": 100,
            "snakes": [(16, 6), (47, 26), (49, 11), (56, 53), (62, 19), (64, 60), (87, 24), (93, 73), (95, 75), (98, 78)],
            "ladders": [(1, 38), (4, 14), (9, 31), (21, 42), (28, 84), (36, 44), (51, 67), (71, 91), (80, 100), (1, 100)],
            "k": 6,
        },
    ]

    for i, test_case in enumerate(test_cases):
        print("---------------------------------------------------")
        print(f"Test Case {i + 1}:")
        size = test_case["size"]
        snakes = test_case["snakes"]
        ladders = test_case["ladders"]
        k = test_case["k"]

        board = SnakesAndLadders(size, snakes, ladders, k)
        
        print("Verifying board conditions:")
        print(f"Can reach goal: {board.canReachGoal()}")
        print(f"No snake/ladder overlaps: {board.noSnakeLadderInSameSquare()}")
        print(f"No direct path from start to end: {board.noDirectPathFromStartToEnd()}")
        print(f"No cycles in the board: {not board.isCyclicBasedOnTopologicalSort()}\n")

        print("Finding shortest path:")
        shortest_path = board.shortestPath()
        
        if shortest_path:
            print(f"Shortest path length: {shortest_path['distance']}")
            print(f"Shortest path: {shortest_path['path']}\n")

            # Simulate dice rolls and plot the histogram
            dice_rolls = [random.randint(1, 6) for _ in range(1000)]
            plot_histogram(dice_rolls)

            # Plot the board with the shortest path highlighted
            

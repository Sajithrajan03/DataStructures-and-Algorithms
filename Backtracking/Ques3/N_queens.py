class N_Queens:
    def issave(self, row, col, board, n):
        a = row
        b = col

        while (row >= 0 and col >= 0):
            if board[row][col] == 'Q':
                return False
            row -= 1
            col -= 1
        col = b
        row = a
        while (col >= 0):
            if board[row][col] == 'Q':
                return False
            col -= 1

        col = b
        row = a
        while (row < n and col >= 0):
            if board[row][col] == 'Q':
                return False
            row += 1
            col -= 1
        return True

    def solve(self, col, board, n, arr, solution_count):
        if col >= n or solution_count[0] == 3:
            arr.append(["".join(i) for i in board])
            solution_count[0] += 1
            return

        for i in range(n):
            if self.issave(i, col, board, n):
                board[i][col] = 'Q'
                self.solve(col + 1, board, n, arr, solution_count)
                board[i][col] = '.'

    def solveNQueens(self, n):
        correct = []
        ans = [["." for _ in range(n)] for _ in range(n)]
        col = 0
        solution_count = [0]  # Counter to keep track of the number of solutions found
        self.solve(0, ans, n, correct, solution_count)

        return correct[:3]  # Return at most 3 solutions


s = N_Queens()
for i in range(4, 9):
    print(f"For N = {i}:\n{s.solveNQueens(i)}\n")

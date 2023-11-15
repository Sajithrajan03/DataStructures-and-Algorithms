class Solution:
    def issave(self,row,col,board,n):
        a = row
        b = col
        
        while (row>=0 and col>=0):
            if board[row][col] == 'Q':
                return False
            row -= 1
            col -= 1
        col = b
        row = a
        while (col>=0):
            if board[row][col] == 'Q':
                return False
            col -= 1
        
        col = b
        row = a
        while (row<n and col>=0):
            if board[row][col] == 'Q':
                return False
            row += 1
            col -= 1
        return True
       
    
    def solve(self,col,board,n,arr):
        if col>=n:
            arr.append(["".join(i) for i in board])
            return
        for i in range(0,n):
            if self.issave(i,col,board,n):
                board[i][col] = 'Q'
                self.solve(col+1,board,n,arr)
                board[i][col] = '.'
    def solveNQueens(self, n):
        correct = list()
        ans = ans = [["." for _ in range(n)] for _ in range(n)]
        col = 0
        self.solve(0,ans,n,correct)
         
        return correct
    
s = Solution()
for i in range(4,9):
    print(f" For N = {i} :\n {s.solveNQueens(i)}\n")

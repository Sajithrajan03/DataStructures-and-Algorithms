class N_Queens:
    def issave(self,col,row,board,n):
        a= row
        b = col
        while(row>=0 and col>=0):
            if board[row][col]=="Q":
                return False
            row-=1
            col-=1
        row = a
        col = b

        while(col>=0):
            if board[row][col]=="Q":
                return False
            col-=1
        row = a
        col = b

        while(row<n and col>=0):
            if board[row][col]=="Q":
                return False
            col-=1
            row+=1

        return True
    def solve(self,col,board,n):
        if col>=n:
            print(board)
            return 
        for  i in range(n):
            if self.issave(col,i,board,n):
                board[i][col] = "Q"
                print(i,col)
                self.solve(col+1,board,n)
                board[i][col] = "."
    
    def N_Queens_solver(self,n):
        ans = [["." for _ in range(n)] for _ in range(n)]
        col = 0
        self.solve(col,ans,n)
s = N_Queens()
s.N_Queens_solver(4)
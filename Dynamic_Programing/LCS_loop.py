class Solution:
    def lcs(self,x,y,i,j,mat,st):
        if i==0 or j ==0:
            return 0
        if mat[i][j] != -1:
            return mat[i][j]
        if str(x[i-1]) == str(y[j-1]):
            st +=str(y[j-1])
            print(st)
            mat[i][j] = 1+self.lcs(x,y,i-1,j-1,mat,st)
            return mat[i][j]
        mat[i][j] = max(self.lcs(x,y,i-1,j,mat,st),self.lcs(x,y,i,j-1,mat,st))
        return mat[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        L = [[None]*(n+1) for i in range(m+1)]
         
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    L[i][j] = L[i-1][j-1]+1
                else:
                    L[i][j] = max(L[i-1][j], L[i][j-1])
    
    
        return L[m][n]
         
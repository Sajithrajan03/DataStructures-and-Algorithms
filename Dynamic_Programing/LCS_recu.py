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
        L = [[-1]*(n+1) for i in range(m+1)]
         
        st=""
    
        return self.lcs(text1,text2,m,n,L,st)
         
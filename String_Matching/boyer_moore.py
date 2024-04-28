def boyer_moore(s,t):
    i = len(t)-1
    j = len(t)-1
    while i<len(s):
        if s[i] == t[j]:
            if j==0:
                return i
            else:
                i-=1
                j-=1
        else:
            i = i+len(t)-min(j,1+s[i:].find(t[j]))
            j = len(t)-1
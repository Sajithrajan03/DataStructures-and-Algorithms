def check(s,t):
    i,j = 0,0
    for i in range(len(s)-len(t)+1):
        print(s[i:i+len(t)],t)
        if s[i:i+len(t)] == t:
            return i
        

print(check("sajith","jith"))
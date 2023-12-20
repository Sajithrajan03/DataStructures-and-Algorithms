def pallindrome(s):
   
    if len(s)<=1:
        return True 
    if s[0]!=s[-1]:
        return False
    
    return pallindrome(s[1:-1])

print(pallindrome("sajith"))
print(pallindrome("malayalam"))
print(pallindrome('madam'))
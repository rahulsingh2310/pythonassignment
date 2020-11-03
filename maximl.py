def smallest_substring(s): 
    i, j, I, J = 0, 0, 0, 0 
    
    H = set([]) 
    while j < len(s): 
        if s[j] in H: 
            H.remove(s[i]) 
            i += 1 
        else: 
            H.add(s[j]) 
            j += 1 
        if J - I < j - i: 
            I, J = i, j 
    return len(s[I:J]) 

str1 = input("Enter string : ") 
print(smallest_substring(str1)) 

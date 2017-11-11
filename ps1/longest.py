def longest(m):
    def is_alphabetical(s):
        for i in range(1,len(s)):
            if s[i]<s[i-1]:
                return False
        return True
    count=0
    
    for i in range(len(m)):
        for j in range(i,len(m)):
            if is_alphabetical(m[i:j+1]) and (j+1-i)>count:
                count=j-i+1
                ret=m[i:j+1]
    return ret
print longest("uvddqndxjqokvcprymwgart")
print longest("vonqugsolesxcur")


                
    
                
            


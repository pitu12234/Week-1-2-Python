hot= False
tall= False

if hot and tall:                               #collons to be in the body or intendation 
    print("he is hot and tall")
elif hot and not tall:                        
    print("he is just but not tall")           
elif not hot and tall:
    print("he is tall but not hot")

else:
    print("he is not hot and tall")
    
    '''''
    KEYWORDS:
    AND WILL RUN IF BOTH THE CONDITIONS TRUE
    OR IF ANY OF IT IS TRUE 
    '''
print("code to print the smallest number")

def smaller(n1,n2,n3):
    if n1<=n2 and n1<=n3:
    
        return  (f"{n1}  is the smallest number")
    elif n2<=n1 and n2<=n3:
       return (f"{n2}  is the smallest number")
       # return n2
    else:
        return (f"{n3}  is the smallest number")
       # return n3
print(min(23,123,3))

#smaller function by python bult in
def smaller_short(n4,n5,n6):
    return n4,n5,n6
print(f"{min(smaller_short(2,4,6))} is the shorter")
def me(name,age,city):
    print(f"i am a guy name {name}, age {age} and live in {city},")

me("mudassar",90,"ohio")

def cube(number): #define a function and gave parameter
    return number **3 #use return to keep the value 

result=cube (3) #the return value is stored in variable
print(result) #we can print out the when we want 

def square(number):
    return number **2
    
result=square(9)
print(result)
result=result-1
print (result)

def guy(name,age,city):
    return (f"the name is {name} and the age is {age } and live in {city}, ")

call=guy ("mudassar",21,"lahore")
print (call)

def add(n1,n2,n3):
    return (f"the addition is {n1+n2+n3}")

print(add(5,5,5))






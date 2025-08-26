number= [12,34,1,67,9,8,12,44]
friends= ["shazeb", "qasim","mudassar", "saad", "umair"]
'''''
friends.extend(number)          #combine two  list
friends.append("tariq")         #adding elements to the list 
friends.insert(1,"bus")         #adding elements in the desire pos
friends.remove("shazeb")       #remove the specific element 
friends.pop()                   #remove the last element of the list by default 
friends.pop(1)                  #remove that element of the index 
friends.clear()                 #clear the whole list 
number.sort()                   #sort list in ascending order
number.reverse()                #reverse the list
print(friends.index("shazeb"))   #to check if the element is in the list 
print (friends.count("umair"))  #check the total number of same elements
friends2=friends.copy()          #copy the list 
print(friends)
'''''
#mystring = input("Give me a string!!!!!!: ")
#print("This is your word: ", mystring)
#count = mystring.count("!")
#print("You have",count, "exclamation points in your word!")
#find_a = mystring.find("T")
#print("the first index of 'T' is at index: ", find_a)
#print(mystring.lower())
#print(mystring.upper())
#print(mystring.replace("Tacos","BORRITOS"))
#print(mystring.strip())
#print(mystring[2:7])
'''
thisIsAList=[1,2,3,4,5]
thisIsAnotherList=["tacos","burritos", "nachos"]
print(thisIsAnotherList)
print(thisIsAnotherList[2])
for f in thisIsAList:
    print(f)

for b in thisIsAnotherList:
    print(b)

thisIsAnotherList.append("quesso")
print(thisIsAnotherList)
thisIsAnotherList.append(65789)
print(thisIsAnotherList)



.append(value) - appends element to end of the list
.count('x') - counts the number of occurrences of 'x' in the list
.index('x') - returns the index of 'x' in the list
.insert('y','x') - inserts 'x' at location 'y'
.pop() - returns last element then removes it from the list
.remove('x') - finds and removes first 'x' from list
.reverse() - reverses the elements in the list
.sort() - sorts the list alphabetically in ascending order, or numerical in ascending order
For a full list please see documentation found at https://docs.python.org/3.1/tutorial/datastructures.html


newlist=[1,4,3,4,5,6,4,8,9,10]
print(newlist.count(4))
print(newlist.index(8))
newlist.sort()
print(newlist)
newlist.insert(9, 'tacos') #inserts before that index slot
print(newlist)
print(newlist.pop()) #removes the last index if you put a index for the arguement it will remove from that index
'''
thisIsATuple = (1,2,3,4,5,6)    #the variables in this tuple can not be changes
print(thisIsATuple)
turnTupleToList= list(thisIsATuple)
turnTupleToList.append(7)
print(turnTupleToList)
turnListToTuple = tuple(turnTupleToList)
print(turnListToTuple)

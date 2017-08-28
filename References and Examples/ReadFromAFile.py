f = open("test.txt", "r") #r is for the read instruction
#print(f.read(1))        #reads the number of characters and removes the character
#print(f.readline())     #reads and removes all the characters til it reaches a newline
#print(f.read())         #reads and removes all the characters

myList=[]               #List to add the whole text file too
for line in f:
    myList.append(line)
#print(myList)
b=len(myList)       #function that gives the entire length of the list
print(b)
for a in range(0,b):
    print(myList[a])

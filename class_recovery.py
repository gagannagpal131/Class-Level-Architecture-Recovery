#package for using regular expressions in the code
import re

#-FUNCTIONS---------------------------------------------------------------------------------
#function to return the index of the parent class, for appending the array classesNames[].
def check_index(classNames,class_name):
    for i in range(0,len(classNames)):
        if classNames[i][0] == class_name:
            return i
        
#Function to display output
def show_output(arr):
    print("Root")
    for i in range(0,2):
        print("  |")
    for i in classNames:
        print("\n   --"+i[0])
        for j in range(1,len(i)):
            print("        |")
            print("        |")
            print("          --"+i[j])
        
        
        
#-MAIN CODE BEGINS---------------------------------------------------------------------------
#this loop is to break single line text into single elements.
with open("demo3.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)
#print(array)
        
#this loop is to break single line text into single elements: 2D Array.      
mystr = []
for i in array:
    if(re.match("class\s+\w+",i)):
        mystr.append(i.split(' '))
#print(mystr)

#this loop is to enter all parent class names in the classNames array.
classNames = []
for i in mystr:
    if 'private' in i:
             print(" ")
    elif 'protected' in i:
            print(" ")
    elif 'public' in i:
            print(" ")
    else:        
        classNames.append([i[i.index("class") + 1]])

#print(classNames)
        
"""
This loop is to insert the child classes in the array classNames[] where the first element of each subarray is the parent.
The second and so on are the child classes of the first parent class in the subarray.
"""
for i in mystr:
    
    if 'private' in i:
        
            class_name = i[i.index('private') + 1]
            #print(class_name)
            my_index = check_index(classNames,class_name)
            #print(my_index)
            classNames[my_index].append(i[i.index("class") + 1])
            
    if 'protected' in i:
        
            class_name = i[i.index('protected') + 1]
            #print(class_name)
            my_index = check_index(classNames,class_name)
            #print(my_index)
            classNames[my_index].append(i[i.index("class") + 1])
        
    if 'public' in i:
        
            class_name = i[i.index('public') + 1]
            #print(class_name)
            my_index = check_index(classNames,class_name)
            #print(my_index)
            classNames[my_index].append(i[i.index("class") + 1])

#function call to display output            
show_output(classNames)

        
        

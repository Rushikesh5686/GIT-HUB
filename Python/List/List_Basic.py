list=[10,20,30,40,50]
#displaying list of elements
print(list)
print()
#displaying elements of list
for i in range(0,len(list),):
    print(list[i])
print()
#displaying type
print(type(list))
print()
#displaying length of list
print('length of list:',len(list))
print()
#accesing list elements
    #indexing
print(list[2])
print(list[4])

    #slicing
print(list[0:len(list):1])
print(list[::])
print(list[2:7:1])
print(list[2:7:])
    #negative indexing
print(list[-1])
print(list[-2])
print(list[-4])
print(list[::-1])
print()
#list methods
    #append element at the end
list.append(12)
list.append(11)
print(list)

    #inserting element at specific index
list.insert(3,66)
list.insert(4,77)
print(list)

    #adding multiple elements to a list
list.extend([66,77,88,99])
print(list)

    #counting repeated occurrences
count1=list.count(66)
print(count1)
count1=list.count(10)
print(count1)
print()
    #return index of an element in a list
print(list)
index=list.index(66)
print("index of 66 is:",index)

index=list.index(50)
print("index of 50 is:",index)
print()

#sorting a list
print("original list:",list)
list.sort()
print("sorted list: ",list)
print()

#sorting a list in reverse order
print("original list:",list)
list.sort(reverse=True)
print("sorted list in reverse order: ",list)
#copy a list 1
list1=list
list1[0]=55
print(list)
print("copy 1",list1)
#copy a list 2
list2=list.copy()
list2[0]=75
print("copy 2",list2)
#reverse a list
print(list) 
list.reverse()
print(list)
#nested list
list3=[[10,20],[30,40]]
for i in range(2):
    for j in range(2):
        print(list3[i][j],end=" ")
    print()    
#concat of list
a=[1,2,3]
b=[4,5,6]
c=a+b
print("Concat of 2 list",c)
#Repetation of list
d=a*3
print("Repetation of list",d)
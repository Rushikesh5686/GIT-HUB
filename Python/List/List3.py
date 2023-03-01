"""Write a Python program to get the largest number from a list. """
l1=[10,20,30,40,50]
max=l1[0]
for x in l1:
    if max<x:
        max=x
print(max)        

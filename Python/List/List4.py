"""Write a Python program to get the smallest number from a list. """
l1=[10,20,30,40,50]
min=l1[0]
for x in l1:
    if min>x:
        min=x
print(min)        

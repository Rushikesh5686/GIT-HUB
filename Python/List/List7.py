"""Write a Python program to remove duplicates from a list"""
l1=[10,20,30,10,20,30,50,60,90,80,70,100,20,50,30,40,50,60,50]
l2=[]
for x in l1:
    if x  not in l2:
        l2.append(x)
l2.sort()        
print(l2)
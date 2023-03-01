"""Write a Python program to find the list of words that are longer than n from a given list of words. """
n=int(input("Enter a length :"))
l1=['a','bb','ccc','dddd','eeeee','ffffff']
l2=[]
for x in l1:
    if len(x)>n:
        l2.append(x)
print(l2)        
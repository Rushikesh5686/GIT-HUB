t1 = (1, 2, 3, 4, 5, 'abc', 1)
print(type(t1))
x = t1.count(1)
print(x)
y = t1.index(4)
print(y)
# WAP to take 5 elements from user(int) & add into list
list = []
for i in range(5):
    x = int(input("enter number"))
    list.append(x)
print(list)
# WAP to print addition of all elements present inside list
list1 = [10, 20, 30, 40, 50]
sum = 0
for i in list1:
    sum += i
print("addition of list element is", sum)
# WAP to find MAX element from thre list
list2 = [101, 20, 30, 40, 505]
# print(sum(list2))
# print(max(list2))
# print(min(list2))
max = list2[0]
for x in list2:
    if x > max:
        max = x
print("MAX number is", max)
# WAP to remove all duplicate elements from list
list3 = [1, 2, 3, 1, 5, 2, 3, 1, 3, 6, 4, 7, 8, 8, 8, 9, 7, 8]
temp = []
for x in list3:
    if x not in temp:
        temp.append(x)
print(temp)

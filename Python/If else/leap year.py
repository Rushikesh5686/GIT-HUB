a=int(input("Enter your  Year"))
if a%4==0 and a%400==0 :
    print("Year is leap")
elif a%100 !=0 :
    print("year is  leap")
else:
    print("Year is not leap")

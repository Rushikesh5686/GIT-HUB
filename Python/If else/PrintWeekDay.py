"""	Write a C program to input week number and print week day.
"""
n=int(input('Enter week number:'))

if n==1 or n==8 or n==15 or n==22 or n==29:
    print("Monday")
elif n==2 or n==9 or n==16 or n==23 or n==30:
    print("Tuesday")
elif n==3 or n==10 or n==17 or n==24:
    print("Wednesday")
elif n==4 or n==11 or n==18 or n==25:
    print("Thursday")
elif n==5 or n==12 or n==19 or n==26:
    print("Friday")
elif n==6 or n==13 or n==20 or n==27:
    print("Saturday")
elif n==7 or n==14 or n==21 or n==28:
    print("Sunday")


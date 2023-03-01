Phy=int(input("enter your Physics marks"))
Chem=int(input("enter your Chemistry marks"))
Bio=int(input("enter your Biology marks"))
Math=int(input("enter your Mathematics marks"))
Comp=int(input("enter your Computer marks"))
Total=Phy+Chem+Bio+Math+Comp
per=(Total/500)*100
print("The Percentage is",per)

if per>=90:
    print("Grade A")
elif per>=80:
    print("Grade B")
elif per>=70:
    print("Grade C")
elif per>=60:
    print("Grade D")
elif per>=40:
    print("Grade E")
else:
    print("Grade F")
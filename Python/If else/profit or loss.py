SP=int(input("Enter your Selling price"))
CP=int(input("Enter your Cost price"))
P=SP-CP
if P>0:
    print("Profit")
elif P==0 :
    print("NO Profit or Loss")
else:
    print("Loss")


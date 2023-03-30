"""Create classes that capture bank customers and bank accounts. A customer has a first and last 
name. An account has a customer and a balance. Make objects for two accounts held by the 
same customer"""


class BankCustomer:
    def __init__(self,fn,ln) -> None:
        self.fn=fn
        self.ln=ln
    
class BankAccount(BankCustomer):
    def __init__(self,fn,ln,bal) -> None:
        super().__init__(fn,ln)
        self.bal=bal
    def showCustomer(self):
        print("First name",self.fn)
        print("Last name",self.ln)
        print("Balance",self.bal)

c1=BankAccount("abc","xyz",1000)
c2=BankAccount("abc","xyz",1500)
c1.showCustomer()
c2.showCustomer()
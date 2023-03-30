"""Create a class that captures airline tickets. Each ticket lists the departure and arrival cities, a 
flight number, and a seat assignment. A seat assignment has both a row and a letter for the seat 
within the row (such as 12F). Make two examples of tickets"""

class Airline:
    def __init__(self,dep,arr,fno,seat) -> None:
        self.dep=dep
        self.arr=arr
        self.fno=fno
        self.seat=seat
    def showTicket(self):
        print("Departure",self.dep)
        print("Arrival city",self.arr)
        print("Flight number",self.fno)
        print("Seat",self.seat)
t1=Airline("Pune to Mumbai","Mumbai",25896,"15G")
t2=Airline("Mumbai to Delhi","Delhi",98563,"16H")
t1.showTicket()
t2.showTicket()
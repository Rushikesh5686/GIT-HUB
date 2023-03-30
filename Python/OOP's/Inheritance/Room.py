"""Create a class “Room” which will hold the “height”, “width” and “breadth” of the room in three 
fields(variables). This class also has a method “volume()” to calculate the volume of this room."""

class Room:
    def __init__(self,height,width,breadth) -> None:
        self.height=height
        self.width=width
        self.breadth=breadth
    def Volume(self):
        v=self.breadth*self.height*self.width
        print("Height of room",self.height)
        print("Breadth of room",self.breadth)
        print("Width of room",self.width)
        print("Volume of room",v)
r1=Room(15,25,16)
r1.Volume()
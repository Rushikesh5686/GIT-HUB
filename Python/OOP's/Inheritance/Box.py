"""Write a class “Box” that with three member-variables “height”, “width” and “breadth”. Write 
suitable constructors to initialize them. Add functions like “getVolume” and “getArea” that will 
return volume and surface area respectively. Create object of boxes and then print their volume 
and surface area"""

class Box:
   def __init__(self,height,width,breadth) -> None:
        self.height=height
        self.width=width
        self.breadth=breadth  
        
   def Volume(self):
        V=self.breadth*self.height*self.width
        print("Volume of box",V)
   def Area(self):
        A=(2*self.breadth*self.width)+(2*self.breadth*self.height)+(2*self.height*self.width)
        print("Area of box",A)    
b1=Box(10,12,8)
b2=Box(30,25,45)
b1.Volume()
b1.Area()
b2.Volume()
b2.Area()
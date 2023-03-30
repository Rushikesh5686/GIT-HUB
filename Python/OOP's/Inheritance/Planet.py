"""Create a class that captures planets. Each planet has a name, a distance from the sun, and its 
gravity relative to Earth’s gravity. For distance and gravity, use the type double which captures 
real numbers. Make objects for Earth and your favorite non-earth planet."""

class Planet:
    def __init__(self,name,dis,gravity) -> None:
        self.name=name
        self.dis=dis
        self.gravity=gravity
    def showPlanet(self):
        print("Name of Planet",self.name)
        print("Distance from the sun",self.dis)
        print("Gravity relative to Earth’s gravity",self.gravity)

p1=Planet("Saturn",100000,24.25)
p2=Planet("Mercury",10000,14.23)
p1.showPlanet()
p2.showPlanet()
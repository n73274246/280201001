class Cylinder:
  def _init_(self,radius,height):
    self.radius = radius
    self.height = height
  def get_radius(self):
    return self.radius
  def get_height(self):
    return self.height
  def set_height(self,height):
    if height >0:
     self.height = height
  def set_radius(self,radius):
    if radius >0:
     self.radius = radius
  def base_area(self):
    import math
    return math.pi*(self.radius**2)
  def surface_area(self):
    import math
    return 2*math.pi*self.radius*self.height
  def area(self):
    return 2*self.base_area()+self.surface_area()
  def volume(self):
    return self.base_area()*self.height

p1 = Cylinder(radius=3,height=5)
print("Area: ",p1.area())
print("Volume: ",p1.volume())


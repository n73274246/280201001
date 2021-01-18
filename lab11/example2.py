class Employee:
  def _init_(self,name,salary):
    self.name = name
    self.salary = salary
  def get_name(self):
    return self.name
  def get_salary(self):
    return self.salary
  def set_name(self,name):
    self.name = name
  def set_salary(self,salary):
    if salary>0:
     self.salary = salary
  def display(self):
    print("Name: "+str(self.name))
  
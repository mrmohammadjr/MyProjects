class car: 
  def __init__(self, cmodel, ccolor , cyear , cspeed):
    self.cmodel = cmodel
    self.ccolor = ccolor
    self.cyear = cyear
    self.cspeed = cspeed
  def car(self):
    print(self.cmodel, self.ccolor, self.cyear, self.cspeed)
    if self.cyear > 2010: 
      print("this car is new")
    else: 
      print("this car is old")
      
c1 = car("bmw i8", "black", 2013, 250)
c2 = car("benz c-class", "silver", 2008, 237)
print(c2.car())
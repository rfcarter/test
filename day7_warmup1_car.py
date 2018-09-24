class Car(): 
  
   def __init__(self, model,  color, tank_size, gallons_of_gas): 
       self.model = model 
       self.color = color
       self.tank_size = tank_size
       self.gallons_of_gas = self.tank_size # We're assuming its tank is full. 

   def drive(self, miles_driven): 
       self.gallons_of_gas -= miles_driven / 10
    
car=Car("Ford", "Blue", 18, 10)
print(car.model, car.color, car.tank_size, car.gallons_of_gas)
car.drive(20)
print(car.model, car.color, car.tank_size, car.gallons_of_gas)
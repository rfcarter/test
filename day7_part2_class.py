class OurClass(): 
    
    def __init__(self, name, location='Platte', size=0): 
        self.name = name
        self.location = location
        self.size = size

our_class=OurClass('Data Science', 'Platte')
print(our_class.name)
print(our_class.location)
print(our_class.size)

our_class=OurClass('Data Science')
print(our_class.name)
print(our_class.location)
print(our_class.size)
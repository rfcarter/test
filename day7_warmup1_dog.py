class DogClass():    
   
    def __init__(self, name, happiness_level=0): 
        self.name = name
        self.happiness_level = happiness_level
 

    def wag_tail(self, times_wagged): 
        for n in range(times_wagged):
            self.happiness_level += 5


    
dog_class=DogClass('Waggles')
print(dog_class.name)
dog_class.wag_tail(12)
print(dog_class.name, dog_class.happiness_level)




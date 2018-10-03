class OurClass():    
    def __init__(self, name, location, size=0): 
        self.name = name
        self.location = location
        self.size = size
        self.questions_asked = []
        if self.size >= 20: 
            self.at_capacity = True
        else: 
            self.at_capacity = False

    def add_question_asked(self, question): 
        self.questions_asked.append(question)


    def add_class_members(self, num): 
        self.size += num

        if self.size >= 20: 
            print('Capacity Reached!!')
            self.at_capacity = True # Now we are saving `at_capacity` to the class itself. 

    def check_if_at_capacity(self): 
        return self.at_capacity

our_class=OurClass('Brewing Class', 'Longmont', 12)
our_class.add_question_asked('What is needed for the class?')
print(our_class.name)
print(our_class.location)
print(our_class.size)
print(our_class.questions_asked)
print("adding 8 to the class")
our_class.add_class_members(8)
our_class.check_if_at_capacity()
print(our_class.size)


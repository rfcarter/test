class OurClass(): 
    
    def __init__(self, name, location): 
        self.name = name
        self.location = location
        self.questions_asked = []

    def add_question_asked(self, question): 
        self.questions_asked.append(question)

our_class=OurClass('Brewing Class', 'Dublin')
print(our_class.name)
print(our_class.location)

our_class.add_question_asked('Where do I start?')
print(our_class.questions_asked[0])

our_class.add_question_asked('What materials do I need to buy?')
print(our_class.questions_asked[1])
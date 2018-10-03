class OurClass():
    def __init__(self, name, location, size=0, members=None):
        self.name = name
        self.location = location
        self.size = size
        self.members = members
        self.at_capacity = False 
        self.class_limit=20
        self.number_of_questions_asked=0

    def add_class_members(self, member):
        self.members.append(member)

    def check_if_at_capacity(self,class_limit):
        if self.size >= self.class_limit:
            self.at_capacity = True
        else:
            self.at_capacity = False
        return self.at_capacity
    
    def count_questions_asked(self,member):
        print("here")
        for row in member:
            print(row.questions_asked)

our_class=OurClass('Intro to Python', 'Platte')



member=[]

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
        for row in member:
            print(row.questions_asked)

    
class Member():
    def __init__(self, member_name, hair_color, birthdate):
        self.member_name = member_name
        self.hair_color = hair_color
        self.birthdate = birthdate
        self.questions_asked=[]
        self.lines_of_code=[]
        self.number_lines_of_code = 0
        self.coding_level = 'beginner'
    
    def add_questions_asked(self, questions_asked):
        self.questions_asked.append(questions_asked)
    
    def add_coded_line(self, lines_of_code):
        self.lines_of_code.append(lines_of_code)
        self.number_lines_of_code += lines_of_code.count('\n')
        Member.get_coding_level(self)

    def get_coding_level(self):
        if self.number_lines_of_code <= 100:
            self.coding_level = 'beginner'
        elif self.number_lines_of_code <= 1000:
            self.coding_level = 'novice'
        elif self.number_lines_of_code <= 10000:
            self.coding_level = 'intermediate'
        else:
            self.coding_level = 'master'

member.append(Member("John", "Brown", "02/12/1980"))
member.append(Member("Bill", "Blond", "07/22/1983"))

# for row in member:
#    print(row.member_name, "has written ", row.number_lines_of_code, "lines of code and is a", row.coding_level)

with open("day7_part3_method1.py") as file:
    sample_code = file.read()
with open("day6_tic_tac_toe.py") as file:
    sample_code2 = file.read()

for row in member:
    if row.member_name == "Bill":
        row.add_coded_line(sample_code)
        row.add_questions_asked("Is there a final?")
        row.add_questions_asked("Is there a mid-term?")
    elif row.member_name == "John":
        row.add_coded_line(sample_code2)
        row.add_questions_asked("Is there a textbook?")

for row in member:
    print(row.member_name, "has written ", row.number_lines_of_code, "lines of code and is a", row.coding_level, row.questions_asked)
our_class=OurClass('Intro to Python', 'Platte')
print(our_class.name, our_class.location)
our_class.count_questions_asked(member)
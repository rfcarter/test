sample_code ="""
my_str = str(input('Enter a string: '))
my_new_str = ""
for idx in range(len(my_str)):
    if idx % 2 == 0:
        my_new_str = my_new_str + my_str[idx].lower()
    else:
        my_new_str = my_new_str + my_str[idx].upper()
print (my_str)
print (my_new_str)
"""

class OurClass():
    def __init__(self, name, location, size=0, members=None):
        self.name = name
        self.location = location
        self.size = size
        self.members = members
        self.at_capacity  

    def add_class_members(self, member):
        self.members.append(member)

    def check_if_at_capacity(self):
        if self.size >= 20:
            self.at_capacity = True
        else:
            self.at_capacity = False
        return self.at_capacity

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
        self.questsion_asked.append(questions_asked)
    
    def add_coded_line(self, lines_of_code):
        self.lines_of_code.append(lines_of_code)
        self.number_lines_of_code += lines_of_code.count('\n')
        Member.get_coding_level(self)

    def get_coding_level(self):
        if self.number_lines_of_code <= 100:
            self.coding_level = 'beginner'
        elif self.number_lines_of_code <= 1000:
            self.coding_level = 'noviVersionn ce'
        elif self.number_lines_of_code <= 10000:
            self.coding_level = 'intermediate'
        else:
            self.coding_level = 'master'

member=Member("John", "Brown", "01/01/1970")
print(member.member_name, "has written ", member.number_lines_of_code, "lines of code and is a", member.coding_level)
member.add_coded_line(sample_code)
print(member.member_name, "has written ", member.number_lines_of_code, "lines of code and is a", member.coding_level)




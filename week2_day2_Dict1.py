usr_input = input("Enter numbers sperated by a dash ")
usr_input=usr_input.replace("-","")
my_dict = {}
for char in usr_input:
    my_dict[char]=(int(char)*int(char))
print(my_dict)
   
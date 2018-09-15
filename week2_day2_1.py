usr_input = input("Enter numbers sperated by comma ")
list1, list2=[], []
usr_input=usr_input.replace(",","")
for idx, char in enumerate(usr_input):
    if idx % 2 == 0:
        list1.append(int(char))
    else:
        list2.append(int(char))
print(list(zip(list1, list2)))



   
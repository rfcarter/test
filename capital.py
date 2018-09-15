my_str = str(input('Enter a string: '))
my_new_str = ""
for idx in range(len(my_str)):
    if idx % 2 == 0:
        my_new_str = my_new_str + my_str[idx].lower()
    else:
        my_new_str = my_new_str + my_str[idx].upper()
print (my_str)
print (my_new_str)



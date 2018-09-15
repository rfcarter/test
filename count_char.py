my_str = str(input('Enter a string: '))
my_char = str(input('Enter a character: '))
count=0
for idx in range(len(my_str)):
    if my_str[idx] == my_char:
        count += 1
print (count)

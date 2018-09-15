my_str = int(input('Enter number '))
my_divisor = int(input('Enter a divisor '))
my_list=""
start_num = 0
for start_num in range(my_str):
    if start_num % my_divisor == 0:
        my_list = my_list + str(start_num) + " "
    else:
        pass
print (my_list)



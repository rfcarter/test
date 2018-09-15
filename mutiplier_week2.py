my_num1 = int(input('Enter number '))
my_num2 = int(input('Enter a second number '))
my_list=""
for my_num1 in range(my_num2):
        my_list = my_list + str(my_num1 * 2) + " "
        print (my_num1*2)
        if (my_num1*2) >= my_num2:
            break
print (my_list)



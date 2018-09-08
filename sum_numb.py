my_num = int(input('Enter a number: '))
sum_result = 0
while my_num > 0:
    sum_result = sum_result +  my_num
    my_num += -1
print ("results: ", sum_result)
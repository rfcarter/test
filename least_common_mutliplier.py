my_num1 = int(input('Enter a number: '))
my_num2 = int(input('Enter a second number: '))
if my_num1 > my_num2:
    greater = my_num1
else:
    greater = my_num2

while(True):
    if((greater % my_num1 == 0) and (greater % my_num2 == 0)):
        lcm = greater
        break
    greater += 1
        
print("least common divisor: ", lcm)
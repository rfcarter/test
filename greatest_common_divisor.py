my_num1 = int(input('Enter a number: '))
my_num2 = int(input('Enter a second number: '))
if my_num1 > my_num2:
        small = my_num2
else:
        small = my_num1
for i in range(1, small+1):
    if((my_num1 % i == 0) and (my_num2 % i == 0)):
        gcd = i
             
print ("Greatest Common Divisor: ",  gcd)
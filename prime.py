import sympy as sy
my_num1 = int(input('Enter a number: '))
if sy.isprime(my_num1) == True:
   print ("This is a prime number: ", my_num1)
else:
   print ("This is not a prime number: ", my_num1)   

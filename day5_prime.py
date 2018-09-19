import sympy as sy
my_num = int(input('Enter a number: '))
for n in range(my_num):
    if sy.isprime(n) == True:
        print ("This is a prime number: ", n)
    else:
        print ("This is not a prime number: ", n)   

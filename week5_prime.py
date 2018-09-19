import sympy as sy

def prime(n):
    if sy.isprime(n) == True:
        print ("This is a prime number: ", n)
    else:
        print ("This is not a prime number: ", n)   

if __name__ == '__main__':
    n=int(input("Input a number to compute the factiorial : "))
    prime(n)
   

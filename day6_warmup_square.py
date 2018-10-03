import math

def perfect_square(nbr):
    x=str(math.sqrt(nbr)).split(".")[1] 
    if x == '0':
        return True
    else:
        return False
    
def next_perfect_square(num):
    x=str(math.sqrt(nbr)).split(".")[0]
    y=(int(x)+1)**2
    return(y) 
   
if __name__ == '__main__':
    nbr=int(input("Please input a number: "))
    ret=perfect_square(nbr) 
    if ret:
        res=next_perfect_square(nbr)
        print(res)
    else:
        print("-1")

    
   
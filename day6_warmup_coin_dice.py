import random

def flip_coin():
    '''
    Input:  None
    Output: Str - 'H' for head or 'T' for tail

    Perform an "experiment" using random.random(), return 'H' if result is above .5, 'T' otherwise.
    '''
    toss = random.random()
    if toss > .5:
       return('H')
    else:
        return('T')
    

def roll_die():
    '''
    Input:  None
    Output: Int - Between 1 and 6

    Using random.randint(), perform a die roll and return the number that "comes up".
    '''
    roll = random.randint(1,6)
    return(roll)

def flip_coin_roll_die(n_times):
    '''
    Input:  Int - number of times to flip a coin and roll a die
    Output: List - of tuples with the outcomes
       of the flips and rolls from each time
    '''
    res=()
    for i in range(n_times):
        res=res+(flip_coin(), roll_die())
    return res

if __name__ == '__main__':
    nbr=int(input("How time to run coin flip and toos dice: "))
    print(flip_coin())
    print(roll_die())
    print(flip_coin_roll_die(nbr))
my_num = str(input('Enter list of numbers: '))
my_div = int(input('Enter a divsor: '))
for n in my_num.split():
    if int(n) % my_div == 0:
        print("yes", int(n), my_div)
    else:
        print("no", int(n), my_div)
my_str = str(input('Enter a string: '))
my_let = str(input('Enter a sub-string: '))
for n in my_str.split():
    if my_let in n:
        print(n)
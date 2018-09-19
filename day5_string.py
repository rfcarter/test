my_str = str(input('Enter a string: '))
my_let = str(input('Enter a letter: '))
for n in my_str.split():
    if n.endswith(my_let):
        print(n)
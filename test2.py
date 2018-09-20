x = ''

def test_func():
    print (x)

def set_global_variable():
   global x
   x = 'abc'

if __name__ == '__main__':
    test_func()
    set_global_variable()
    test_func()
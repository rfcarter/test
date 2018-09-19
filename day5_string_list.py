def string_list(s):
    l=[]
    for w in s.split():
        l.append(tuple((w,len(w))))
    print(l) 
if __name__ == '__main__':
    s=str(input("Input a string : "))
    string_list(s)

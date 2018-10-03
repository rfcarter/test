def word_count(w, d):
    count = 0
    word_count = 0
    for word in w:
        print (word)
        if word != d:
            count += 1
        else:
            word_count += 1
            count=0
    if count > 0:
        word_count += 1
    print ("number of words :", word_count)

if __name__ == '__main__':
    w=str(input("Input s sentence : "))
    d=str(input("Input a delimiter: "))
    word_count(w,d)

   

def count_xo(word:str):
    word_x = []
    word_o = []
    for i in word:
        if i == 'o':
            word_o.append(i)
        elif i == 'x':
            word_x.append(i)
    return word_o,word_x,len(word_o) == len(word_x)





word:str = input("Enter the word:")
print(count_xo(word))
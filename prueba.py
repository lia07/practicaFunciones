string1 = input('Introduce a string : ')
string2 = input('Introduce other string : ')

lenght1 = len(string1)
lenght2 = len(string2)

if lenght1 > lenght2 :
    print('The word: ',string1, ' has ',lenght1-lenght2,' characters more than the word: ', string2)
else:
    print('The word: ', string2, ' has ', lenght2 - lenght1, ' characters more than the word: ', string1)
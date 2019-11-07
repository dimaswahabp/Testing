'''
for i in range(1,11):
    if i % 2  == 0:
        print('WOW!')
    else:
        print(i)
'''
'''def fizzbuzz(x):
    for i in range (1, x+1):
        if (i % 3 ) == 0 and (i%5) == 0 :
            print('fizzbuzz')
        elif (i % 5) == 0:
            print("buzz")
        elif(i%3) == 0:
            print("fizz")
        else:
            print(i)

fizzbuzz(15)
'''
'''
vocalWords = list('aiueo')
print (vocalWords)

def changeVocal(param):
    newString =''
    for i in param:
        if i in vocalWords:
            i ='o'
            newString += i
        else:
            newString += i
    print(newString)

changeVocal(input('masukan kalimat :').lower())
'''
'''
mandy = input("masukan kata : ")
def palin (kata):
    if kata[::-1] == kata:
        print(True)
    else:
        print(False)
palin(mandy)
'''

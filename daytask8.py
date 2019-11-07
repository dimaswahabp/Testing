'''#star
def star(x):
    star = ' '
    for i in range(x):
        star += ' * '
        print(star)

star(5)
'''
'''
#star
def rstar(x):
    star = ' '
    for i in range(x):
        star = ' * ' * (x-i)
        print(star)

rstar(5)
'''
'''
#star
def rnumber(x):
    number = ' '
    for i in range(x):
        angka = 1 + i
        number = str(angka) +' '
        print(number)

rnumber(5)
'''
'''
#star
def rnumber(x):
    number = ' '
    for i in range(x):
        angka = x - i
        number = (str(angka)+' ') * (x-i) 
        print(number)

rnumber(5)
'''
'''
#star
def rnumber(x):
    number = ' '
    for i in range(x):
        angka = 1 + i
        number = (str(angka)+' ') * (1+i) 
        print(number)

rnumber(5)
'''
#star
'''
def rnumber(x):
    number = ' '
    for i in range(x):
        angka = 1 + i
        number = (str(angka)+' ') * (x-i) 
        print(number)

rnumber(5)
'''
'''
#star
def rnumber(x):
    number = ' '
    for i in range(x):
        angka = x - i
        number += (str(angka)+' ')
        print(number)

rnumber(5)
'''

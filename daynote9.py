#python : Lambda function
'''
x = lambda a,b,c : a+b+c
def y(a,b,c):
    return a+b+c

print(x(2,3,4))
print(y(2,3,4))
'''
'''
x = lambda a : 'Amgka Genap' if a % 2 == 0 else 'Angka Ganjil'
def y(a):
    if a % 2 == 0:
        return True
    else:
        return False
print(x(4))
print(y(4))
'''
'''
#map python
def y(a):
    return len(a)
a = ['andibogieman', 'lala', 'caca']

x = map(y, a)
print(x)
print(list(x))
'''
'''
a = ['cokelat', 'melon', 'nangka']
b = ['apel', 'jeruk', ]
'''
'''
x = [2,4,6,8,10]
def pangkat2(a):
    return a ** 2
y = map(pangkat2, x)
print(list(y))

z = map(lambda a:a**2, x)
print(list(z))
'''
nomor = [1-100]
=> angka genap filter
[2,4,6,8,10....100]
=> setiap angka genap x2 map
[4,8,12,...200]
=> semua angka hasilnya dijumlahkan satu sama lain reduce
4+8+12+ ... 2000 = ???

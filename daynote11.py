'''
class Manusia:
    def __init__(self,nama):
        self.nama = nama
class Pria(Manusia):
    def __init__(self,nama,gender):
        Manusia.__init__(self,nama)
        self.gender = 'Laki -Laki'
class Wanita(Manusia):
    def __init__(self,nama,gender):
        Manusia.__init__(self,nama)
        self.gender = 'Wanita'
Y
objA = Manusia('Bambang')
objB = Pria('Bambang', 'laki - Laki')
objC = Wanita('Niken', 'Wanita')
print(vars(objA))
print(vars(objB))
print(vars(objC))
'''
'''
class X:
    def __init__(self,x):
        self.x = x
class Y(X):
    def __init__(self,x,y):
        X.__init__(self,x)
        self.y = y
class Z(Y):
    def __init__(self,x,y,z):
        Y.__init__(self,x,y)
        self.z= z
objA = Z('bambang', 'pns', True)
print(vars(objA))
'''

'''
class Karnivora:
    def __init__(self):
        self.daging = True
        self.nama = 'Karnivora'
class Herbivora:
    def __init__(self):
        self.tumbuhan = True
        self.nama = 'Herbivora'
class Omnivora(Karnivora,Herbivora):
    def __init__(self):
        Karnivora.__init__(self)
        Herbivora.__init__(self)
        self.mcd = True
        self.nama = 'Omnivora'
objA = Omnivora()
print(vars(objA))
print(Omnivora.__mro__)
'''
'''
import datetime as dt 
x = dt.datetime.now()
print(x.strftime('%d')) #tgl
print(x.strftime('%A')) #hari
print(x.strftime('%m')) #bulan
print(x.strftime('%B')) #nama bulan
print(x.strftime('%Y')) #thn
print('---------------------')
print(x.strftime('%H')) #24
print(x.strftime('%I')) #12
print(x.strftime('%p')) #am/pm
print(x.strftime('%M')) #min
print(x.strftime('%S')) #sec
print('---------------------')



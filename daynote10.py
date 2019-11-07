#class = cetakan object
'''
class Mobilcustom():
    def __init__(self,warna,tahun,model):
        self.color = warna
        self.year = tahun
        self.model = model
#method
def jadul(self):
    if.self.year < 2019:
        return True
    else: return False
def tes(self):
    print
mobil1 = Mobilcustom('pink', 2018,'sedan')
mobil2 = Mobilcustom('blue',2018, 'SUV')
mobil3 = Mobilcustom('blue',2018, 'City car')

print(mobil1.color)
print(mobil2.year)
print(mobil3.model)
'''
from pprint import pprint
class student:
    def __init__(self,nama,usia):
        self.nama = nama
        self.usia = usia
    
data = [
    {'nama': 'andi', 'usia' : 21},
     {'nama': 'budi', 'usia' : 22},
      {'nama': 'caca', 'usia' : 23},
       {'nama': 'deni', 'usia' : 24},
]

Tem =  []
for i in data:
    Tem.append(student(i.get('nama'), i.get('usia')))
for obj in Tem:
    pprint(obj.__dict__)

pprint(Tem[0].nama)
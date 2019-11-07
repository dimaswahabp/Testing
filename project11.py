
'''
import datetime as dt 
x = dt.datetime.now()

class time:
    def __init__(self,x):
        self.hari = x.strftime('%A')
        self.tanggal = x.strftime('%d') 
        self.bulan = x.strftime('%B') 
        self.tahun = x.strftime('%Y')
        self.jam = x.strftime('%H')
        self.menit= x.strftime('%M')
        self.detik = x.strftime('%S')
 '''
from stastitika import kane 
angka = [1,3,9,2,6,4,7,8,5,5]
myStat = kane(angka)
print("mean :", myStat.getMean())
print("Median :", myStat.getMedian())
print("Mode :", myStat.getMode())


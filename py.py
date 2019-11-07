from project11 import time
import datetime as dt 
x = dt.datetime.now()
now = time(x)

print(now.hari)
print(now.tanggal)
print(now.bulan)
print(now.tahun)
print(now.jam)
print(now.menit)
print(now.detik)

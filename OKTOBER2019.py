nama = 'Hari ini Hari tidak masuk sekolah'
# jumlah huruf 'h'
cari = 'h'
x = nama.upper().replace(cari.upper(), '')
print(x)
JmlCari = Len(nama) - len(x)
print(f'Jumlah huruf \'{cari}\' ada = {JmlCari}'')

#Jumlah Kata 'Hari' ?
cari = 'sekolah'
x = nama.upper().replace(cari.upper()), '')
print (x)
JmlCari = int((len(nama) - len(x)) / len(cari))
print(f'Jumlah huruf \'{cari}\' ada = {JmlCari}'')
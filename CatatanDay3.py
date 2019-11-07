# x = 12
# x = 13
# x += 2
# x -= 2
# x *= 2
# x /= 2
# print(x)

# x ='abcdefghijklmnopqrstuvwyz'
# #print(x[::2])
# #print('g' in x)
# #print(x.count('g'))
# kalimat = 'Hari ini Andi tidak kuliah'
# cari = 'h'
# print(cari.lower() in kalimat.lower())
# print(kalimat.lower().count(cari.lower()))

# #list
# x = ['Miranti', 'Rista', 'Yunia', 'Adrea', 'Devita']
# print(type(x))

# #nampilin list keberapa yang mau diambil
# print(x[1])
# print(x[len(x) - 2])
# print(x[-1])

# #contoh
#hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
# print(hari[5])

#sekarang hari 'rabu', hari apakah 100 hari rabu lagi?
hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']

now = 'rabu'; brphari = -1;
inow = hari.index(now)
sisaHari = brphari % len(hari)
hariygdicari = hari []
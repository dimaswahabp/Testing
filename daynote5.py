'''
#dictionary
andi = {

'name': 'Andi',
'age': 22,
'is_married': False
'job': 'pns', 
'cars': ['Alphard', 'Xpander', 'Innova'],
'address': {
                'street' : 'Mawar Ungu'
                'RT' : 5, 'RW' : 121, 'Kecamatan': 'X',
                'zipcode' : 123456,
                'geo' : { 
                    'lat': 111.11,
                    'lng' : 65.89


                }




}


}
print(list(andi))
print(list(andi.keys()))
print(list(andi.values()))
'''
'''
andi['salary'] = 25000000
andi.update({'no_ktp' : 1234567890})
print(andi)
'''

'''
print(andi ['name'])
print(andi ['age'])
print(andi ['is_married'])
print(andi.get('name'))
print(andi.get('age'))
print(andi.get('is_married'))

print(andi.get('job', 'Maaf Andi masih nganggur'))
andi = ['name'] = 'budi'
print(andi)
'''
days = {
'senin': 'Monday', 'selasa': 'tuesday', 'Rabu': 'wenesday',
'kamis': 'thursday', 'Jumat': 'friday', 'sabtu': 'Saturday', 'minggu': 'sunday'

}
'''
days
hari = input('Ketik nama hari : ')
print(f'{hari.upper()} = {days.get(hari.lower(), "ga ada!")}')
'''
daysKeys = list(days.keys()) #daftar indo
daysValues = list(days.values())

day = input("type the day :")
artinya = daysKeys[daysValues.index(day)]
print(f"bahasa of {day.upper()}g = {artinya.upper()}")

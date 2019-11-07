
'''
students = ['Andi', 'Budi', 'Caca'] 

def tes(x):
    print(x[0])
    print('Caca'in x)

tes(students)
'''
'''
students = ['Andi', 'Budi', 'Caca', 'Deni']
index = 0
while index <= len(students) - 1:
    print(students[index])
    index += 1
'''
'''
x =[1,2,3,4,5,6,7,8,9,10]
y = []
index = 0
while index <= len(x)-1:
    y.append(x[index]**2)
    index += 1

print(y)
'''
i = 1
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1



i = 0
while i < 10:
    i+=1
    if i == 5:
        continue

print(i)

password = '12345'
status = False
if input ('Masukan Password: ') != password:
    while status == False:
        userInput == input("password salah!, Ketik Password: ")
        if(userInput == password):
            status = True
            print('password Benar')
        else:
            status = False
else:
    print('password benar!')


    
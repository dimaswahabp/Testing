#sebuah function dengan 1 parameter
#function => menentukan value parameter ganjil genap
'''
def gangen(x):
    if (x % 2) == 0:
        print (f"{x} adalah bilangan genap")
    else :
        print(f"{x} adalah bilangan ganjil")

gangen(11)
'''
'''
#Sebuah function calc
def calc():
    x = float(input('Masukan Angka 1 :'))
    op = input('Masukan operator (+-*/) ')
    y = float(input('Masukan Angka 2 :'))
    if op == '+':
        print(x+y)
    elif op == '-':
        print(x-y)
    elif op == '*':
        print(x*y)
    elif op == '/':
        print(x/y)
    else:
        print("Sori Sori Jek")
calc()    
'''
def vocal(kata):
    kata = kata.replace("a","o")
    kata = kata.replace("i","o")
    kata = kata.replace("u","o")
    kata = kata.replace("e","o")
    print(kata)

vocal(input("masukan kata :"))

a = list('abcde')
b = list('bcfgh')
#a n b = {b,c}
a = set(a)
b = set(b)
'''
print(a.intersection(b))
print(b.intersection(a))
print(a & b)
print(b & a)
'''
#union
'''
print(a.union(b))
print(b.union(a))
print (a | b)
print (b | a)
'''
#selisih
'''
print(a.difference(b))
print(b.difference(a))
print (a - b)
print (b - a)
'''
'''
print (a.symmetric_difference(b))
print (b.symmetric_difference(a))
print (a ^ b)
print (b ^ a)
'''
'''
P  = set([1,2,4,7,9,19])
Q  = set([5,7,9,19,6,12,16,17])
R  = set([3,6,8,19])

print (P & Q)
print (P & Q & R)
'''
'''
P = []
Q = []
R = []
S = []

for i  in range (-1,8,1):
    S.append(i)

for i  in range (-9,10,1):
    P.append(i)

for i  in range (-1,7,1):
    R.append(i)

for i  in range (-4,5,1):
    Q.append(i)

print(sorted(set(P)))
print(set(Q))
print(set(R))
'''
S = []
A = (2,3,5,7)
B = {5,7,9}

for i  in range (0,11,1):
    S.append(i)

#C
A = set(A)
B = set(B)
S = set(S)
print(A & B)

#D
print (A | B)

#E
print (A & (A | B))

#F
print (B & (A | B))

#G
print ((A |B) & (A | B))

#H
print ((A & B) | (A | B))
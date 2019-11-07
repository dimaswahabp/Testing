#bikin program yang mengubah kata menjadi morse
def sandi(x):
    morse = {
        'A' : '.-',
        'B' : "-…",		
        "C" : "-.-.",	
        "D" : "-…",		
        "E" : "."	,	
        "F" : "..-.",	
        "G" : "–.",		
        "H" : "….",		
        "I" : "..",		
        "J" : ".—",		
        "K" : "-.-",		
        "L" : ".-..",		
        "M" : "—",		
        "N" : "-.",
        "O" : "—",
        "P" : ".–..",
        "Q" : "–.-",
        "R" : ".-.",
        "S" : "…",
        "T" : "–",
        "U" : "..-",
        "V" : "…-",
        "W" : ".–",
        "X" : "-..-",
        "Y" : "-.–",
        "Z" : "–..",
        ' ' : '/'
        }
    key = list(morse)
    value = list(morse.values())
    y = []
    for i in x:
        if i.upper() in key:
            z = value[key.index(i.upper())]
        y.append(z)
    print(''.join(y))

sandi('Aku cinta kamu')
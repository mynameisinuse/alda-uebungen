# hashfunktion of exercise 2
def hhash(s: str)->str: # s ist ein Schlüssel vom Typ string
    '''A simple hash function.'''
    # hash wird mit 0 iniyialisiert
    h = 0
    for k in s:
        h = 23*h + ord(k) # Aktualisieren des Hashs mit dem Zeichencode
    return h

def checkfilesums(path: str):
    s =[]
    with open(path,'r') as f:
        for line in f:
            s.append(hhash(line))
    for i in s:
        assert(i == s[0])

if __name__ == "__main__":
    import itertools as it
    s = [chr(33+9-i)+chr(i*23) for i in range(2,c+1)]
    
    with open('collision.txt','w') as f:
        result = it.product(s, repeat=2)
        for i in result:
            f.write(i[0]+i[1]+'\n')

    checkfilesums("collision.txt")

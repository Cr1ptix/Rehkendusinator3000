from random import randint

def uus_tehe():
    #Kas liitmine või lahutamine
    i = randint(0, 1)
    x = "+"
    if i == 0:
        i = -1
        x = "-"
    a = randint(0, max_arv)
    b = randint(0, a)
    
    tekst = str(a) + x + str(b) + "= ?"
    lahendus = a + i * b
    return [tekst, lahendus]

global max_arv
max_arv = 10
while True:
    y = uus_tehe()
    print(y[0])
    answer = input()
    if int(answer) == y[1]:
        print("õige")
        max_arv += 2
        uus_tehe()
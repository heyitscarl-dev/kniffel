from random import randint


wuerfels = [0, 0, 0, 0, 0]

for i in range(5):
    wuerfels[i] = randint(1, 6)

print(wuerfels)

def wurf_Mensch():
    behalten_str = str(input("Welche willst du behalten?"))
    behalten_lst = behalten_str.split(",")
    
    for i in range(5):
        if len(behalten_lst)==5:
            return False

        if not str(wuerfels[i]) in behalten_lst:
            wuerfels[i] = randint(1, 6)
        else:
            behalten_lst.remove(str(wuerfels[i]))
    
    print(wuerfels)
    return True

if wurf_Mensch() == True:
    wurf_Mensch()

#bot ist dran

def wurf_Bot():
    anzahl_behalten = randit(1, 5)
    
    
   




# Ausgeben

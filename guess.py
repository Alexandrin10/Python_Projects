import random
tries = 0
numar = random.randint(1,100)
print("Hmm... ai curajul sa incearci sa ghicesti la ce numar ma gandit de la 1 la 100 :D ")
while tries <6:
    jucatorul=int(input("Zi numarul:)  "))
    tries+=1
    if jucatorul < numar:
        print('Numarul tau e prea mic:),mai incearca ')
        
    if jucatorul > numar:
        print("Numarul tau e prea mare :)  ")
        
    if jucatorul == numar:
        print("Felicitari ai ghicit esti cel mai bravo :D")
        break
        
    if  jucatorul != numar and tries == 6:
        print(f"Scuze :( cu parere de rau nu ai ghicit ,numarul meu este: {numar}")
        break
        
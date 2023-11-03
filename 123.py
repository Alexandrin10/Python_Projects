import random

continui = True

while continui:
    alegerea_jucatorului = input("Alegeti P(piatra), F(foarfece), Fo(foaie): ").lower()

    if alegerea_jucatorului not in ["p", "f", "fo"]:
        print("Incorect,incearca din nou: ")
    else:
        alegerea_pc = random.choice(["p", "f", "fo"])
        print(f"Alegerea Pc-ului = {alegerea_pc}")

        if alegerea_jucatorului == alegerea_pc:
            print("Este egal")
        elif (alegerea_jucatorului, alegerea_pc) in [("p", "f"), ("f", "fo"), ("fo", "p")]:
            print("Ai castigat ;) ")
        else:
            print("Ai pierdut :( ")

    raspuns = input("Doresti sa continui [D/N] ").lower()
    continui = raspuns == 'd'

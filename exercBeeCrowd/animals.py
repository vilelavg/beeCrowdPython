tip=input("Vertebrado ou invertebrado: ")
if tip == 'vertebrado':
    tip2=input("ave ou mamifero: ")
    if tip2 == 'ave':
        tip3=input("Carnivoro ou onivoro: ")
        if tip3 == 'carnivoro':
            print("aguia")
        elif tip3 == 'onivoro':
            print("pombo")
    elif tip2 == 'mamifero':
        tip3=input("onivoro ou herbivoro: ")
        if tip3 == 'onivoro':
            print("homem")
        elif tip3 == 'herbivoro':
            print("vaca")
elif tip == 'invertebrado':
    tip2=input("inseto ou anelideo: ")
    if tip2 == 'inseto':
        tip3=input("Hematofago ou herbivoro: ")
        if tip3 == 'hematofago':
            print("pulga")
        elif tip3 == 'herbivoro':
            print("lagarta")
    elif tip2 == 'anelideo':
        tip3=input("hematofago ou onivoro: ")
        if tip3 == 'hematofago':
            print("sanguessuga")
        elif tip3 == 'onivoro':
            print("minhoca")
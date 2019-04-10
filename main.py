import random

lista_tkb = ["9:00-13:00", "13:00-17:00"]



#print(lista[1])

#for k,v in lista_dni.items():
i = 0
for i in range(4):

    lista = ["Aleksandra Walczak", "Sandra Radzimska", "Damian Karasiński", "Andrzej Wróbel", "Adrian Sowiński",
                  "Norbert Ucieszyński", "Mateusz Czarnecki", "Paweł Fornalczyk", "Mariusz Kieler", "Maciej Wójtowicz",
                  "Jarosław Boguta"]
    lista_dni = {"Poniedziałek": 4, "Wtorek": 4, "Środa": 4, "Czwartek": 4, "Piątek": 4}
    pon = []
    wt = []
    sr = []
    czw = []
    pt = []
    print("NOWA PETLA !!!!!!!!!!!!!!!!!!!!!!!!")
    #print("lista osob", lista)
    #print(lista_dni)

    print("Tydzień: ", i)
    i += 1
    print("Poniedziałek")

    while lista_dni["Poniedziałek"] > 0:

        if len(lista) > 0:
            x = random.choice(lista)
            lista_dni["Poniedziałek"] -= 1
            pon.append(x)
            print("osoba: ", x)
            lista.remove(x)
            continue
        else:

            lista = ["Aleksandra Walczak", "Sandra Radzimska", "Damian Karasiński", "Andrzej Wróbel", "Adrian Sowiński",
                     "Norbert Ucieszyński", "Mateusz Czarnecki", "Paweł Fornalczyk", "Mariusz Kieler",
                     "Maciej Wójtowicz",
                     "Jarosław Boguta"]
            for index in range(len(pon)):
                index = 0
                lista.remove(pon[index])
                pon.remove(pon[index])
                index += 1
            continue
    print("Wtorek")

    while lista_dni["Wtorek"] > 0:

        if len(lista) > 0:
            lista_dni["Wtorek"] -= 1
            x = random.choice(lista)

            wt.append(x)
            print("osoba: ", x)
            lista.remove(x)
        else:

            lista = ["Aleksandra Walczak", "Sandra Radzimska", "Damian Karasiński", "Andrzej Wróbel",
                     "Adrian Sowiński",
                     "Norbert Ucieszyński", "Mateusz Czarnecki", "Paweł Fornalczyk", "Mariusz Kieler",
                     "Maciej Wójtowicz",
                     "Jarosław Boguta"]
            for index in range(len(wt)):
                index = 0
                lista.remove(wt[index])
                wt.remove(wt[index])
                index += 1

    print("Środa")

    while lista_dni["Środa"] > 0:
        #print("lista", len(lista))
        if len(lista) > 0:
            lista_dni["Środa"] -= 1
            x = random.choice(lista)

            sr.append(x)
            print("osoba: ", x)
            lista.remove(x)
        else:

            lista = ["Aleksandra Walczak", "Sandra Radzimska", "Damian Karasiński", "Andrzej Wróbel",
                     "Adrian Sowiński",
                     "Norbert Ucieszyński", "Mateusz Czarnecki", "Paweł Fornalczyk", "Mariusz Kieler",
                     "Maciej Wójtowicz",
                     "Jarosław Boguta"]
            for _ in range(len(sr)):
                index = 0
                #print("lista: ", lista)
                #print("LISTA SR", sr)
                #print("TUUUU ", sr[index])
                lista.remove(str(sr[index]))
                sr.remove(sr[index])
                index += 1
            continue

    print("Czwartek")

    while lista_dni["Czwartek"] > 0:

        if len(lista) > 0:
            lista_dni["Czwartek"] -= 1
            x = random.choice(lista)

            czw.append(x)
            print("osoba: ", x)
            lista.remove(x)
        else:

            lista = ["Aleksandra Walczak", "Sandra Radzimska", "Damian Karasiński", "Andrzej Wróbel",
                     "Adrian Sowiński",
                     "Norbert Ucieszyński", "Mateusz Czarnecki", "Paweł Fornalczyk", "Mariusz Kieler",
                     "Maciej Wójtowicz",
                     "Jarosław Boguta"]
            for index in range(len(czw)):
                index = 0
                lista.remove(czw[index])
                czw.remove(czw[index])
                index += 1

    print("Piątek")

    while lista_dni["Piątek"] > 0:

        if len(lista) > 0:
            lista_dni["Piątek"] -= 1
            x = random.choice(lista)

            pt.append(x)
            print("osoba: ", x)
            lista.remove(x)
        else:

            lista = ["Aleksandra Walczak", "Sandra Radzimska", "Damian Karasiński", "Andrzej Wróbel",
                     "Adrian Sowiński",
                     "Norbert Ucieszyński", "Mateusz Czarnecki", "Paweł Fornalczyk", "Mariusz Kieler",
                     "Maciej Wójtowicz",
                     "Jarosław Boguta"]
            for index in range(len(pt)):
                index = 0
                lista.remove(pt[index])
                pt.remove(pt[index])
                index += 1

        # print(lista)
        # print("nowa" ,lista_dni["Poniedziałek"])


    #
    # print("Wtorek")
    #
    # while lista_dni["Wtorek"] > 0:
    #     lista_dni["Wtorek"] -= 1
    #     x = random.choice(lista)
    #     print("osoba: ", x)
    #     lista.remove(x)
    #     # print(lista)
    #     # print("nowa" ,lista_dni["Poniedziałek"])
    #
    # print("Środa")
    # while lista_dni["Środa"] > 0:
    #     lista_dni["Środa"] -= 1
    #     x = random.choice(lista)
    #     print("osoba: ", x)
    #     lista.remove(x)
    #     # print(lista)
    #     # print("nowa" ,lista_dni["Poniedziałek"])
    #
    # print("Czwartek")
    # while lista_dni["Czwartek"] > 0:
    #     lista_dni["Czwartek"] -= 1
    #     x = random.choice(lista)
    #     print("osoba: ", x)
    #     lista.remove(x)
    #     # print(lista)
    #     # print("nowa" ,lista_dni["Poniedziałek"])
    #
    # print("Piątek")
    # while lista_dni["Piątek"] > 0:
    #     lista_dni["Piątek"] -= 1
    #     x = random.choice(lista)
    #     print("osoba: ", x)
    #     lista.remove(x)
    #     # print(lista)
    #     # print("nowa" ,lista_dni["Poniedziałek"])
    # i += 1
    # #print(lista)

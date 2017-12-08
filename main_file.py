from bardagi import *
from character import *
import os


nafn = input("Hvert er nafnið þitt? ")

while True:
    kyn = input("1. Maður\n"
          "2. Dvergur\n"
          "3. Álfur\n"
          "Hver viltu vera? ")
    if kyn.isdigit():
        kyn = int(kyn)
        if kyn >= 1 and kyn <= 3:
            break
        else:
            print("Er ekki 1, 2 eða 3")

    else:
        print("Er ekki tala")


ovinir=[{"stats":{"styrkur":4,"heilsa":10},"equipment":{"járn öxi":{"value":4,"verd":1200,"tegund":"vopn"},"járn brynja":{"value":4,"verd":750,"tegund":"brynja"}}},
        {"stats":{"styrkur":6,"heilsa":20},"equipment":{"járn öxi":{"value":6,"verd":1200,"tegund":"vopn"},"járn brynja":{"value":6,"verd":750,"tegund":"brynja"}}},
        {"stats":{"styrkur":8,"heilsa":30},"equipment":{"járn öxi":{"value":8,"verd":1200,"tegund":"vopn"},"járn brynja":{"value":8,"verd":750,"tegund":"brynja"}}},
        {"stats":{"styrkur":10,"heilsa":40},"equipment":{"járn öxi":{"value":10,"verd":1200,"tegund":"vopn"},"járn brynja":{"value":10,"verd":750,"tegund":"brynja"}}},
        {"stats":{"styrkur":12,"heilsa":50},"equipment":{"járn öxi":{"value":12,"verd":1200,"tegund":"vopn"},"járn brynja":{"value":12,"verd":750,"tegund":"brynja"}}},]
spilari = character(nafn, kyn)

while True:
    if len(ovinir)<=0:
        print("ÞÚ VANNST")
        break
    print(spilari)
    print()
    print("1. Halda áfram\n"
          "2. Fara í búð\n"
          "3. Birgðir\n"
          "4. Sofa(15 gull)")
    valmynd = input(">> ")
    print()
    # Bardagi
    if valmynd == "1":
        while True:
            enemy=ovinir[0]["stats"]
            enemy_equipment=ovinir[0]["equipment"]
            bardaginn=bardagi(spilari.stats(),spilari.hlutr,spilari.inventory,enemy,enemy_equipment)
            ovinur_heilsa = enemy["heilsa"]
            ovinur_heilsa = str(ovinur_heilsa)
            print("ýttu á Enter til að kasta tening"
                  "\nveldu 1 til að bæta heislu")
            # velja hvort að að berjast eða bæta heilsu til að þú deyrð ekki.
            velja=input(">>")
            if velja=="1":
                spilari.health=bardaginn.heilsa()
            # Ef það er ekki valið 1
            else:
                enemy["heilsa"]=bardaginn.bardaginn_notandi()
            bardaginn = bardagi(enemy, enemy_equipment,spilari.inventory, spilari.stats(), spilari.hlutr)
            spilari.health=bardaginn.bardaginn_ovinur()

            print("Heilsa:", spilari.stats()["heilsa"])

            if enemy["heilsa"]<=0:
                print("Þú drapst óvininn")
                del ovinir[0]
                gull=randint(1,1000)
                print("Þú fannst",gull,"gull")
                spilari.gold+=gull
                break

            elif spilari.stats()["heilsa"]<=0:
                print("Þú tapaðir")
                break

            print("Heilsa óvinarins:", enemy["heilsa"])
            print("-----------------------")

    # Búð
    if valmynd == "2":
        while True:
            # Allir hlutirnir í búðinni
            vopn = {"brons sverð": {"value": 4, "verd": 200, "tegund": "vopn"}
                , "járn sverð": {"value": 8, "verd": 1000, "tegund": "vopn"}
                , "járn öxi": {"value": 10, "verd": 1200, "tegund": "vopn"}
                , "mithril brynja": {"value": 20, "verd": 5000, "tegund": "brynja"}
                , "járn brynja": {"value": 4, "verd": 750, "tegund": "brynja"}
                ,  "betri járn bryna":{"value": 10, "verd": 1750, "tegund": "brynja"}}
            # Prentar vopnin og eiginleika þeirra
            for x in vopn:
                v = vopn[x]
                if v["tegund"] == "sverð" or v["tegund"] == "öxi":
                    print(x, "dmg:", v["value"], "verð:", v["verd"], "tegund:", v["tegund"])
                else:
                    print(x, "block:", v["value"], "verð:", v["verd"], "tegund:", v["tegund"])

            # Kaupir vopn
            while True:
                kaupa = input("Veldu það sem þú vilt kaupa(1 til að hætta) ")
                til = False
                for x in vopn:
                    v = vopn[x]
                    if x.lower() == kaupa.lower():
                        til = True
                        if spilari.gold >= v["verd"]:
                            spilari.gold -= v["verd"]
                            spilari.inventory[kaupa.lower()] = v
                            print(spilari.inventory)
                        else:
                            print("Þú átt ekki nóg gull\n"
                                  "auli")
                            break

                if kaupa == "1":
                    break

                if til != True:
                    print("Ekki til")

                else:
                    break


            valmynd = input("1. Búð\n"
                            "2. Út\n"
                            ">> ")
            if valmynd == "2":
                break

    # Hvað spilari hefur og þar sem er skipt á milli
    if valmynd == "3":
        print("Geymt")
        for x in spilari.inventory:
            print(x, spilari.inventory[x])

        print("\nValið")
        for x in spilari.hlutr:
            print(x, spilari.hlutr[x])
        input("\nEnter til að halda áfram")
        while True:
            breyta=input("Hvað viltu velja? (1 til að hætta)")
            if breyta=="1":
                break
            # Gáir hvort að spilari er með hlutinn
            for x in spilari.inventory:
                if x==breyta:
                    print(spilari.inventory[x]["tegund"])
                    # Gáir hvort að það sé vopn eða brynja
                    if spilari.inventory[x]["tegund"]=="vopn":
                        # Fer í gegn um hluti og leitar af vopni
                        for y in spilari.hlutr:
                            if spilari.hlutr[y]["tegund"]=="vopn":
                                # Tekur úr inventory og setur í hluti
                                spilari.inventory[y]=spilari.hlutr[y]
                                del spilari.hlutr[y]
                                spilari.hlutr[x]=spilari.inventory[x]
                                del spilari.inventory[x]
                                break

                    elif spilari.inventory[x]["tegund"]=="brynja":
                        for y in spilari.hlutr:
                            if spilari.hlutr[y]["tegund"]=="brynja":
                                spilari.inventory[y]=spilari.hlutr[y]
                                del spilari.hlutr[y]
                                spilari.hlutr[x]=spilari.inventory[x]
                                del spilari.inventory[x]
                                break
                    else:
                        print("Ekki vopn eða brynja")

        print("\nGeymt")
        for x in spilari.inventory:
            print(x, spilari.inventory[x])

        print("\nValið")
        for x in spilari.hlutr:
            print(x, spilari.hlutr[x])
        input("\nEnter til að halda áfram")

    # Sefur með óréttlæti
    if valmynd == "4":
        if spilari.kyn == "Maður":
            spilari.gold -= 15
            spilari.health = 20

        if spilari.kyn == "Dvergur":
            spilari.gold -= 20
            spilari.health = 30

        if spilari.kyn == "Álfur":
            spilari.gold -= 30
            spilari.health = 25

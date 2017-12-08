from bardagi import *
from character import *
import os

spilari = character("Jón", 1)
print(spilari)
enemy={"styrkur":10,"heilsa":20,"dext":10}
enemy_equipment={"járn öxi":{"value":8,"verd":1200,"tegund":"vopn"},"járn brynja":{"value":6,"verd":750,"tegund":"brynja"}}

while True:
    bardaginn=bardagi(spilari.stats(),spilari.hlutr,enemy,enemy_equipment)
    ovinur_heilsa = enemy["heilsa"]
    ovinur_heilsa = str(ovinur_heilsa)
    enemy["heilsa"]=bardaginn.bardaginn_notandi()
    bardaginn = bardagi(enemy, enemy_equipment, spilari.stats(), spilari.hlutr)
    spilari.stats()["heilsa"]=bardaginn.bardaginn_ovinur()

    print("Heilsa:", spilari.stats()["heilsa"])
    if enemy["heilsa"]<=0:
        print("Þú drapst óvininn")
        break

    elif spilari.stats()["heilsa"]<=0:
        print("Þú tapaðir")
        break

    print("Heilsa óvinarins:", enemy["heilsa"])
    print("-----------------------")
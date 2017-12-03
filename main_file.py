from bardagi import *
from character import *

spilari = character("Jón", 1)
print(spilari)
enemy={"styrkur":10,"heilsa":20,"dext":10}
enemy_equipment={"járn öxi":{"value":8,"verd":1200,"tegund":"vopn"},"járn brynja":{"value":2,"verd":750,"tegund":"brynja"}}

while True:
    bardaginn=bardagi(spilari.stats(),spilari.hlutr,enemy,enemy_equipment)
    enemy["heilsa"]=bardaginn.bardaginn_notandi()
    bardaginn = bardagi(enemy, enemy_equipment, spilari.stats(), spilari.hlutr)
    print(enemy)
    spilari.stats()["heilsa"]=bardaginn.bardaginn_ovinur()
    print("Högg stig", spilari.stats()["heilsa"])
    if enemy["heilsa"]<=0:
        print("Þú drapst óvininn")
        break
    elif spilari.stats()["heilsa"]<=0:
        print("Þú tapaðir")
        break
    print("Heilsan þín:",spilari.stats()["heilsa"])
    print("Heilsa óvinarins:", enemy["heilsa"])
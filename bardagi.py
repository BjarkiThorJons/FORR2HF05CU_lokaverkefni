from random import *
character={"styrkur":20,"heilsa":30,"dext":10}
character_equipment={"járn öxi":{"value":8,"verd":1200,"tegund":"öxi","notun":"vopn"},"járn brynja":{"value":30,"verd":750,"tegund":"brynja","notun":"vernd"}}
enemy={"styrkur":10,"heilsa":20,"dext":10}
enemy_equipment={"járn öxi":{"value":8,"verd":1200,"tegund":"öxi","notun":"vopn"},"járn brynja":{"value":30,"verd":750,"tegund":"brynja","notun":"vernd"}}
class bardagi:
    def __init__(self,stats_1,equipment_1,stats_2,equipment_2):
        self.s1=stats_1
        self.e1=equipment_1
        self.s2=stats_2
        self.e2=equipment_2
    def bardaginn_notandi(self):
        styrkur_1=self.s1["styrkur"]
        heilsa_2 = self.s2["heilsa"]
        input("Kastaðu tening til að hitta (ýttu á enter)")
        kast_1=randint(1,20)
        print(kast_1)
        for x in self.e1:
            if self.e1[x]["notun"]=="vopn":
                dmg_1=self.e1[x]["value"]
        for x in self.e2:
            if self.e2[x]["notun"]=="vernd":
                vernd_2=self.e2[x]["value"]
        print(kast_1,styrkur_1,vernd_2)
        if kast_1+styrkur_1>=vernd_2:
            print("Þú hittir")
            input("Kastaðu tening til að meiða (ýttu á enter)")
            kast_2=randint(1,dmg_1)
            heilsa_2=heilsa_2-kast_2
            print("Þú meiddir fyrir:",kast_2)
            return heilsa_2
        else:
            return heilsa_2
    def bardaginn_ovinur(self):
        styrkur_1=self.s1["styrkur"]
        heilsa_2 = self.s2["heilsa"]
        input("Óvinurinn kastar tening til að hitta")
        kast_1=randint(1,20)
        print(kast_1)
        for x in self.e1:
            if self.e1[x]["notun"]=="vopn":
                dmg_1=self.e1[x]["value"]
        for x in self.e2:
            if self.e2[x]["notun"]=="vernd":
                vernd_2=self.e2[x]["value"]
        print(kast_1,styrkur_1,vernd_2)
        if kast_1+styrkur_1>=vernd_2:
            print("Óvinurinn hittir")
            input("Óvinurinn kastar tening til að meiða (ýttu á enter)")
            kast_2=randint(1,dmg_1)
            heilsa_2=heilsa_2-kast_2
            print("Óvinurinn meiddi fyrir:",kast_2)
            return heilsa_2
        else:
            return heilsa_2
while True:
    bardaginn=bardagi(character,character_equipment,enemy,enemy_equipment)
    enemy["heilsa"]=bardaginn.bardaginn_notandi()
    bardaginn=bardagi(enemy,enemy_equipment,character, character_equipment)
    print(enemy)
    character["heilsa"]=bardaginn.bardaginn_ovinur()
    print(character)
    if enemy["heilsa"]<=0:
        print("Þú drapst óvininn")
        break
    elif character["heilsa"]<=0:
        print("Þú tapaðir")
        break
    print("Heilsan þín:",character["heilsa"])
    print("Heilsa óvinarins:",enemy["heilsa"])


from random import *

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
        for x in range(9):
            print("")

        kast_1=randint(1,20)

        for x in self.e1:
            if self.e1[x]["tegund"]=="vopn":
                dmg_1=self.e1[x]["value"]

        for x in self.e2:
            if self.e2[x]["tegund"]=="brynja":
                vernd_2=self.e2[x]["value"]

        # Prentar kastið hjá notenda og sýnir vernd hjá óvini
        utkoma = kast_1 + styrkur_1
        print("þú kastaðir fyrir {0}\n"
              "{1} + {0} = {2}\n"
              "Vernd hans er {3}".format(kast_1,styrkur_1, utkoma,vernd_2))

        if kast_1+styrkur_1>=vernd_2:
            print("Þú hittir")
            print("-----------------------")
            input("Kastaðu tening til að meiða (ýttu á enter)")
            for x in range(11):
                print("")
            kast_2=randint(1, dmg_1)
            heilsa_2=heilsa_2-kast_2
            print("Þú meiddir fyrir:", kast_2)
            print("{0} - {1} = {2}".format(self.s2["heilsa"], kast_2, heilsa_2))
            print("Óvinur er nú með {0} í heilsu".format(heilsa_2))
            return heilsa_2

        else:
            return heilsa_2

    def bardaginn_ovinur(self):
        styrkur_1=self.s1["styrkur"]
        heilsa_2 = self.s2["heilsa"]
        input("Óvinurinn kastar tening til að hitta(enter)")
        kast_1=randint(1,20)
        for x in range(8):
            print("")

        for x in self.e1:
            if self.e1[x]["tegund"]=="vopn":
                dmg_1=self.e1[x]["value"]

        for x in self.e2:
            if self.e2[x]["tegund"]=="brynja":
                vernd_2=self.e2[x]["value"]

        utkoma = kast_1 + styrkur_1
        print("Óvinur kastar fyrir {0}\n"
              "{1} + {0} = {2}\n"
              "Vernd þin {3}".format(kast_1, styrkur_1, utkoma, vernd_2))
        if kast_1+styrkur_1>=vernd_2:

            print("Óvinurinn hittir")
            print("-----------------")
            print("Óvinurinn kastar tening til að meiða")
            for x in range(10):
                print("")

            kast_2=randint(1, dmg_1)
            heilsa_2=heilsa_2-kast_2
            print("Óvinurinn meiddi fyrir:", kast_2)
            return heilsa_2

        else:
            return heilsa_2
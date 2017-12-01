class character:
    def __init__(self, nafn, kyn):
        # Maður
        if kyn == 1:
            strength = 6
            health = 20
            gold = 1000
            equipment = {"Járnsverð":{"value":8, "verð":1000, "tegund":"vopn"}, "Járn brynja":{"value":25, "tegund":"brynja"}}
            inventory = {"vatn":{"value":6,"tegund":"heilsa","magn":2}, "Kjöt":{"value":6, "tegund":"heilsa", "magn":1}}

        # Dvergur
        if kyn == 2:
            strength = 10
            health = 30
            gold = 500
            equipment = {"Gullexi":{"value":6, "verð":0, "tegund":"vopn"}, "Leður brynja":{"value":15, "tegund":"brynja"}}
            inventory = {"Öl":{"value":5, "tegund":"heilsa", "magn":1}, "Brauð":{"value":5, "tegund":"heilsa", "magn":1}}

        # Álfur
        if kyn == 3:
            strength = 8
            health = 25
            gold = 750
            equipment = {"Spjót":{"value":7, "verð":200, "tegund":"vopn"}, "Brynja":{"value":20, "tegund":"brynja"}}
            inventory = {"Heilsu flaska":{"value":10,"tegund":"heilsa", "magn":1},"brauð":{"value":5, "tegund":"heilsa", "magn":2}}

        self.nafn = nafn
        self.strength = strength
        self.health = health
        self.gold = gold
        self.hlutr = equipment
        self.inventory = inventory

    def __str__(self):
        inv = ""
        print(next(iter(self.inventory)))
        for x in self.inventory:
            if len(self.inventory) == 1 or next(iter(self.inventory)) == x:
                inv += x
            else:
                inv += ", {item}".format(item = x)

        return "\nNafn: {nafn}\n" \
               "Hefur styrkisgildið {strength} \n" \
               "Heilsugildið er {health} \n" \
               "Gull: {gold} \n" \
               "valið {val}" \
               "Birgðir: {inventory}".format(nafn = self.nafn, strength = self.strength, health = self.health, gold = self.gold, val = self.hlutr, inventory = inv)

    def stats(self):
        stats = {"styrkur":self.strength, "heilsa":self.health, "gold":self.health, "inv":self.inventory, "hlutir":self.hlutr}
        return stats
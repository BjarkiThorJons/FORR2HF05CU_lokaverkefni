class character:
    def __init__(self, nafn, kyn):
        # Humna
        if kyn == 1:
            strength = 10
            health = 10
            gold = 100
            dexterity = 15
            inventory = {"sheep":{"value": 10, "price": 20}}

        # Dvergur
        if kyn == 2:
            strength = 20
            health = 30
            gold = 50
            dexterity = 10
            inventory = {"lamb":{"value": 5, "price": 10}}

        # Álfur
        if kyn == 3:
            strength = 15
            health = 20
            dexterity = 13
            gold = 75
            inventory = {"Water":{"value":7, "price": 15},"fire":{"value":3}}

        self.nafn = nafn
        self.strength = strength
        self.health = health
        self.gold = gold
        self.dext = dexterity
        self.inventory = inventory
    def __str__(self):
        inv = ""
        print(next(iter(self.inventory)))
        for x in self.inventory:
            if len(self.inventory) == 1 or next(iter(self.inventory)) == x:
                inv += x
            else:
                inv += ", {item}".format(item = x)

        return "\nÞitt nafn er {nafn}\n" \
               "hefur styrkisgildið {strength} \n" \
               "heilsugildið er {health} \n" \
               "Gull: {gold} \n" \
               "Handlagn: {dext} \n" \
               "Birgðir: {inventory}".format(nafn = self.nafn, strength = self.strength, health = self.health, gold = self.gold, dext = self.dext, inventory = inv)
    def bardagi(self):
        stats = {"styrkur":self.strength, "heilsa":self.health, "gold":self.health, "dext": self.dext, "inv":self.inventory}
        return stats


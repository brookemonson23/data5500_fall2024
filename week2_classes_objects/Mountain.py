#self refers an object itself
class Mountain:
    def __init__(self, name, ht, miles, elevation):
        self.name = name
        self.ht = ht
        self.miles = miles
        self.elevation = elevation
    
    def __str__(self):
        return "Mount " + self.name + ", elevation; " + str(self.elevation) + " ft."
    
mt_rainier = Mountain("Rainier", 5000, 4, 75000)

print(mt_rainier)

half_dome = Mountain("Half Dome", 10000, 9, 13000)

print(half_dome)


class MiniGolfPlayers:
    def __init__(self, name, status, avgholes, favfood):
        self.name = name
        self.status = status
        self.avgholes = avgholes
        self.favfood = favfood

    def __str__(self):
        return "This mini golf playa is named " + str(self.name) + ", has the status of " + str(self.status) + ", averages " + str(self.avgholes) + " shots per hole, and loves to eat " + str(self.favfood) + "!!!"
    
tommyboy = MiniGolfPlayers("tommy", "elite", 2, "pasta")

print(tommyboy)
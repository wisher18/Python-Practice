class Cricket:
    no_of_matches = 10
    def __init__(self, name, runs):
        self.name = name
        self.runs = runs
    def printdet(self):
        print(f"Playeer name is {self.name}, and runs are {self.runs}")

class Odi(Cricket):
    def __init__(self, name , strike):
        self.name = name
        self.strike= strike

Virat = Cricket("Virat", 1000)
Rohit = Odi("ROhit", 100.12)
Virat.printdet()










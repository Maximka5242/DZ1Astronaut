from random import randint

class Astronaut:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.energy = 50
        self.morale = 50
        self.alive = True
        self.stability_station = 50
        self.progress = 0

    def explore(self):
        print("Time to explore")
        self.morale += 5
        self.energy -= 5
        chance_travma = randint(1, 5)
        if chance_travma == 1:
            self.health -= 20
            print("Під час експедиції ви отримали травму!")
        else:
            print("Експедиція успішна!")

    def repair(self):
        print("I will repair")
        self.morale -= 3
        self.energy -= 3
        self.stability_station += 10

    def rest(self):
        print("Rest time")
        self.energy += 10
        self.progress += 3

    def communicate(self):
        print("Communicate")
        self.morale += 3
        self.energy -= 4

    def is_alive(self):
        if self.health <= 0:
            print("Ви померли...")
            self.alive = False
        elif self.energy <= 0:
            print("У вас немає енергії...")
            self.alive = False
        elif self.morale <= 0:
            print("У вас не лишилось глузду...")
            self.alive = False

    def end_of_day(self, day):
        print("\n" + "-" * 20)
        print(f"Day: {day}")
        print(f"Health: {self.health}")
        print(f"Energy: {self.energy}")
        print(f"Morale: {self.morale}")
        print(f"Station Stability: {self.stability_station}")
        print(f"Progress: {self.progress}")
        print("-" * 20 + "\n")

    def live(self, day):
        if not self.alive:
            return
        action = randint(1, 4)
        if action == 1:
            self.explore()
        elif action == 2:
            self.repair()
        elif action == 3:
            self.rest()
        elif action == 4:
            self.communicate()
        self.end_of_day(day)
        self.is_alive()

astronaut_Nazar = Astronaut("Nazar")
for day in range(1, 366):
    if not astronaut_Nazar.alive:
        break
    astronaut_Nazar.live(day)

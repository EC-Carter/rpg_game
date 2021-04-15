# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__(self):
        pass

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self,attacked):
        if attacked.type == "zombie":
            attacked.health = attacked.health
        else:
            attacked.health -= self.power 
            print(f"{self.name} does {self.power} damage to {attacked.name}.")
            if attacked.health <= 0:
                print(f"{attacked.name} is dead.")

    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.power} power.")

class Hero(Character):
    def __init__(self, name):
        self.health = 10
        self.power = 5
        self.name = name
        self.type = "hero"

class Goblin(Character):
    def __init__(self, name):
        self.health = 6
        self.power = 2
        self.name = name
        self.type = "goblin"

class Zombie(Character):
    def __init__(self, name):
        self.health = 1
        self.power = 4
        self.name = name
        self.type = "zombie"

    def alive(self):
        return True
        

emmit = Hero("emmit")
hyacinth = Goblin("hyacinth")
richard = Zombie("richard")

def main():
    # if playing with the goblin
    #while hyacinth.alive() and emmit.alive():

    #if playing with the zombie
    while emmit.alive() and richard.alive():
        emmit.print_status()
        #hyacinth.print_status()
        richard.print_status()
        print()
        print("What do you want to do?")
        print("1. fight zombie")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        choice = input()
        if choice == "1":
            emmit.attack(richard)  
        elif choice == "2":
            pass
        elif choice == "3":
            print("Run, run, run....")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if richard.health > 0:
            richard.attack(emmit)
main()
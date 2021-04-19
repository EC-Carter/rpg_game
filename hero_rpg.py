
import random

#Character class and subclasses
class Character:
    def __init__(self,name,health,power,coins):
        self.health = health
        self.power = power
        self.name = name
        self.coins = coins

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def prob(self, percent_chance):
        rand = random.randint(1,10)
        if rand > percent_chance:
            return True
        else:
            return False
    
    def print_status(self):
        print(f"{self.name} the {self.type} has {self.health} health and {self.power} power.")

    def power_up(self, power_up_by):
        power_level = self.power * power_up_by
        return power_level
        
    def attack_shadow(self,attacked, power_level):
        if self.prob(9):
            attacked.health -= power_level
            print(f"{self.name} does {power_level} damage to {attacked.name}.")
            if attacked.alive() == False:
                print(f"{attacked.name} is dead.\n")
                self.coins += attacked.coin_bonus
                print(f"the bounty for killing {attacked.name} is\n{attacked.coin_bonus} coins. You have {self.coins} coins!")
        else:
            print(f"{attacked.name} got away.\n")

    def attack_zombie(self, attacked, power_level):
        attacked.health -= power_level 
        print(f"{self.name} does {power_level} damage to {attacked.name}.")
        print(f"but {attacked.name} is not dead.\nneed {self.name} braaaaaiiiins...\n")
    
    def attack_alchemist(self,attacked, power_level):
        attacked.health -= power_level
        print(f"{self.name} does {power_level} damage to {attacked.name}.")
        if self.prob(7) and self.coins > 5:
            self.coins -= 5
            attacked.coins += 5
            print(f"{attacked.name} stole 5 of our coins.\nYour now have {self.coins} coins")
            if attacked.alive() == False:
                print(f"{attacked.name} is dead.\n")
                self.coins += attacked.coins * 2
                print(f"the bounty for killing {attacked.name} is\n{attacked.coins * 2} coins. You have {self.coins} coins!")
        else:
            if attacked.alive() == False:
                print(f"{attacked.name} is dead.\n")
                self.coins += attacked.coins * 2
                print(f"the bounty for killing {attacked.name} is\n{attacked.coins * 2} coins. You have {self.coins} coins!")

    def attack(self, attacked, power_level ):
        if attacked.type == "shadow":
            self.attack_shadow(attacked,power_level)
        elif attacked.type == "zombie":
            self.attack_zombie(attacked,power_level)
        elif attacked.type == "alchemist":
            self.attack_alchemist(attacked, power_level)
        else:
            attacked.health -= power_level 
            print("The results of the battle are:")
            print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
            print(f"{self.name} does {power_level} damage to {attacked.name}.\n")
            if attacked.alive() == False:
                print(f"{attacked.name} is dead.\n")
                self.coins += attacked.coin_bonus
                print(f"the bounty for killing {attacked.name} is\n{attacked.coin_bonus} coins. You have {self.coins} coins!")
                print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
                print()

    def vil_attack(self,attacked):
        if attacked.armor > 0:
            attacked.health -= (self.power - attacked.armor)
            print(f"{self.name} attacked {attacked.name}")
            print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
            print(f"{self.name} does {self.power - attacked.armor} damage to {attacked.name}.\n")
            if attacked.alive() == False:
                print(f"{attacked.name} is dead.\n")
                print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
                print()
        elif attacked.evade > 0:
            if attacked.evade == 2:
                if self.prob(9):
                    print(f"{attacked.name}s evade points helped them avoid attacks this time.\n")
                else:
                    self.vil_attack_base(attacked)
            elif attacked.evade == 4:
                if self.prob(8):
                    print(f"{attacked.name}s evade points helped them avoid attacks this time.\n")
                else:
                    self.vil_attack_base(attacked)
            elif attacked.evade >= 6:
                if self.prob(7):
                    print(f"{attacked.name}s evade points helped them avoid attacks this time.\n")
                else:
                    self.vil_attack_base(attacked)
        else:
            self.vil_attack_base(attacked)

    def vil_attack_base(self, attacked):
        attacked.health -= self.power
        print(f"{self.name} attacked {attacked.name}")
        print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
        print(f"{self.name} does {self.power} damage to {attacked.name}.\n")
        if attacked.alive() == False:
            print(f"{attacked.name} is dead.\n")
            print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
            print()

    def buy(self,item):
        if item.price <= self.coins:
            if isinstance(item, Weapon) or isinstance(item,Potion):
                self.bag.append(item)
                self.coins -= item.price
                print(f"{item.name} is in your bag. You have {self.coins} coins left.")
            elif isinstance(item,Armor):
                self.coins -= item.price
                self.armor += item.power
                print(f"{item.power} {item.name} points have been added.\nYou have {self.coins} coins left.")
            elif isinstance(item,Evade):
                self.coins -= item.price
                self.evade += item.power
                print(f"{item.power} {item.name} points have been added.\nYou have {self.coins} coins left.")
        else:
            print(f"You do not have enough coins to buy {item.name}")

    def show_coins(self):
        print(f"You have {self.coins} coins")
        print(f"You have {self.evade} evade points")
        print(f"You have {self.armor} armor points")

    def bag_status(self):
        if len(self.bag) > 0:
            for i in self.bag:
                if i.uses == 0:
                    self.bag.remove(i)
                    print(f"you've used up {i.name}")
            print(f"{i.name} has {i.uses} more uses")
        else:
            print(f"You have nothing in your bag.")

    def char_reset(self):
        self.power = self.base_power

    def bees(self):
        self.health -= 2
        print(f"A swarm of angry bees attacked {self.name}.\nTheir health decreases by 2.")
    
    def caravan(self):
        if self.evade >= 2:
            self.evade -= 2
            print(f"A Carvan of nosiy followers will not leave {self.name} alone.\nTheir evade points decrease by 2.")
        else:
            print(f"A Carvan of nosiy followers will not leave {self.name} alone.\nToo bad {self.name} dosen't have any evade points. ")
    
    def rust(self):
        if self.armor >= 1:
            self.armor -= 1
            print(f"Magic rust ate away {self.name}s Armor. Their armor points decrease by 1.")
        else:
            print(f"Magic rust tried to get {self.name}. Too bad you don't have any armor.")

class Hero(Character):
    def __init__(self, name, health = 10, power = 5, coins = 10):
        super().__init__(name, health, power, coins)
        self.type = "hero"
        self.armor = 0
        self.evade = 0
        self.bag = []
        self.base_power = 5

    def attack(self, attacked):
        power_level = 0
        if super().prob(8):
            power_level = super().power_up(2)
            
        else:
            power_level = self.power
        super().attack(attacked,power_level)

    def hero_bag_menu(self):
        for c , i in enumerate(self.bag):
            print(f"{c +1}. {i.name}")

        choice = input("Choose a number or '9' to exit > ")

        for c , i in enumerate(self.bag):
            if int(choice) == c + 1:
                i.use(self)
                print(f"{i.name} is activated")
                main()
            elif choice == "9":
                main()

class Goblin(Character):
    def __init__(self, name, health = 6, power = 2, coins = 0):
        super().__init__(name, health, power,coins)
        self.type = "goblin"
        self.coin_bonus = 2

class Zombie(Character):
    def __init__(self, name, health = 1, power = 4, coins = 0):
        super().__init__(name, health, power,coins)
        self.type = "zombie"
        self.coin_bonus = 0
    
    def alive(self):
            return True

class Medic(Character):
    def __init__(self, name, health = 12, power = 3, coins = 0):
        super().__init__(name, health, power,coins)
        self.type = "medic"
        self.coin_bonus = 2

    def recuperate(self):
        if super().prob(8) and super().alive():
            self.health += 2
            print(f"{self.name} healed and now has {self.health} health.\n")

class Shadow(Character):
    def __init__(self, name, health = 1, power = 7, coins = 0):
        super().__init__(name, health, power, coins)
        self.type = "shadow"
        self.coin_bonus = 7

class Alchemist(Character):
    def __init__(self, name, health = 8, power = 3, coins = 3): 
        super().__init__(name, health, power, coins)
        self.type = "alchemist"
        self.coin_bonus = coins * 2

class Giant(Character):
    def __init__(self, name, health = 10, power = 8, coins = 0):
        super().__init__(name, health, power, coins)
        self.type = "giant"
        self.coin_bonus = 6

##########################################
#item class and subclasses
class Item:
    def __init__(self,name,power,price):
        self.name = name
        self.power = power
        self.price = price
        
    def use(self,character):
        characterAttr = getattr(character, self.instance_var)
        if self.oper == "add":
            characterAttr += self.power
            setattr(character, self.instance_var, characterAttr)
            verb = "added"
        elif self.oper == "sub":
            characterAttr -= self.power
            verb = "subtracted"
            setattr(character, self.instance_var, characterAttr)
        elif self.oper == "mulit":
            characterAttr *= self.power
            verb = "multiplied"
            setattr(character, self.instance_var, characterAttr)
        self.uses -= 1
        print(f"{character.name} used {self.name} and {verb} {self.power}\npoints to their {self.instance_var} ")
        print(f"{character.name} has {getattr(character, self.instance_var)} {self.instance_var}")

class Armor(Item):
    def __init__(self,name,power,price):
        super().__init__(name, power, price)

class Evade(Item):
    def __init__(self,name,power,price):
        super().__init__(name, power, price)

class Potion(Item):
    def __init__(self,name,power,price,oper,inst_var,uses):
        super().__init__(name, power, price)
        self.oper = oper
        self.instance_var = inst_var
        self.uses = uses

class Weapon(Item):
    def __init__(self,name, power, price,uses):
        super().__init__(name, power, price)
        self.uses = uses

    def use(self,character):
        character.power += self.power
        print(f"The {self.name} is ready to use. It adds {self.power} to your fight.")
        self.uses -= 1
        #print(f"You have {self.uses} uses of the {self.name} left after this")

# instances of characters and items 
##########################################
#items
armor = Armor("armor",2,10)
helmet = Armor("helmet",1,5)
evade = Evade("evade",2,5)

super_tonic = Potion("super tonic",10, 5,"add","health",1)
great_sword = Weapon("great sword",3,10,7)
#characters
emmit = Hero("emmit")
hyacinth = Goblin("hyacinth")
richard = Zombie("richard")
elizabeth = Medic("elizabeth")
vicar = Shadow("vicar")
daisy = Alchemist("daisy")
rose = Giant("rose")
char_list = [emmit,hyacinth,richard,elizabeth,vicar,daisy,rose]

# Game logic
##########################################

def main():
    
    while Hero.alive(emmit):
        print()
        print("The Candle Light Supper is Coming...\nWhat do you want to do?")
        print("- - - - - - - - - -")
        Hero.show_coins(emmit)
        Hero.bag_status(emmit)
        print("- - - - - - - - - -")
        for char in char_list:
            if char.alive():
                char.print_status()
            else:
                print(f"{char.name} the {char.type} is dead")
        print()
        print("""1. fight zombie
2. fight goblin
3. fight medic
4. fight shadow
5. fight alchemist
6. fight giant
7. do nothing
8. buy stuff
9. draw weapon
10. flee
- - - - - - - - - -""")
        print("> ", end=' ')

        choice = input()

        if choice == "1":
            Hero.attack(emmit,richard)
            Hero.char_reset(emmit)
            #Hero.bag_status(emmit)
        elif choice == "2":
            Hero.attack(emmit,hyacinth)
            Hero.char_reset(emmit)
            #Hero.bag_status(emmit)
        elif choice == "3":
            Hero.attack(emmit,elizabeth)
            Medic.recuperate(elizabeth)
            Hero.char_reset(emmit)
            #Hero.bag_status(emmit)
        elif choice == "4":
            Hero.attack(emmit,vicar)
            Hero.char_reset(emmit)
            #Hero.bag_status(emmit)
        elif choice == "5":
            Hero.attack(emmit,daisy)
            Hero.char_reset(emmit)
            #Hero.bag_status(emmit)
        elif choice == "6":
            Hero.attack(emmit,rose)
            Hero.char_reset(emmit)
            #Hero.bag_status(emmit)
        elif choice == "7":
            pass
        elif choice == "8":
            store()
        elif choice == "9":
            weapon_menu()
        elif choice == "10":
            #print("Run, Run, Run...")
            break
        else:
            print(f"Invalid input {choice}")
        villan_attack()

def villan_attack():
    num = random.randint(1,10)

    if richard.alive() and num == 1:
        richard.vil_attack(emmit)
    elif hyacinth.alive() and num == 2:
        hyacinth.vil_attack(emmit)
    elif rose.alive() and num == 3:
        rose.vil_attack(emmit)
    elif vicar.alive() and num == 4:
        vicar.vil_attack(emmit)
    elif daisy.alive and num == 5:
        daisy.vil_attack(emmit)
    elif elizabeth.alive() and num == 6:
        elizabeth.vil_attack(emmit)
    elif (elizabeth.alive() and hyacinth.alive()) and num == 7:
        elizabeth.vil_attack(emmit)
        hyacinth.vil_attack(emmit)
    elif num == 8:
        Hero.bees(emmit)
    elif num == 9:
        Hero.caravan(emmit)
    elif num == 10:
        Hero.rust(emmit)

def store():

    print("Coin Status:")
    Hero.show_coins(emmit)
    print("Bag Status:")
    Hero.bag_status(emmit)
    print()
    print("What do you want to buy?")
    print("- - - - - - - - - -")
    print("""1. Super Tonic - adds 10 to health - 5 coins
2. Great Sword - adds 3 power for 7 uses - 7 coins
3. Armor - adds 2 armor points for rest of the game - 10 coins
4. 2 Evade points  - Chance to evade attack rises the more you have - 5 points 
5. Helmet - adds 1 armor point for the rest of the game - 5 coins
6. Buy nothing - Back to the battle""")
    print("> ", end=' ')
    
    choice = input()
    if choice == "1":
        Hero.buy(emmit,super_tonic)
    elif choice == "2":
        Hero.buy(emmit,great_sword)
    elif choice == "3":
        Hero.buy(emmit,armor)
    elif choice == "4":
        Hero.buy(emmit,evade)
    elif choice == "5":
        Hero.buy(emmit,helmet)
    elif choice == "6":
        main()
    else:
        print(f"Invalid input {choice}")
    main()

def weapon_menu():
    Hero.bag_status(emmit)
    print("- - - - - - - - - -")
    print("What do you want to use?")
    print("- - - - - - - - - -")
    Hero.hero_bag_menu(emmit)

main()
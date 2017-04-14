from random import randint

class Player(object):

    def health(self):
        health_amount = self
        health_amount = 50
        return health_amount

    def attack(self):
        attack_amount = self
        attack_amount = randint(1,10)
        return attack_amount

    def potions(self):

        """Used every battle that healing is possible in so you don't have to
           type out the code every time.
        """

        potions = self
        potions = 0
        return potions

        if potions >= 1 and action.lower() == "use potion":
            print "You drink all of the red liquid from the bottle and heal for"
            print "15 health."
            player_health += 15

            if player_health > 50:
                player_health = 50


class Monster(object):

    def health(self):
        health_amount = self

    def attack(self):
        attack_amount = self


class Goblin(Monster):

    def health(self):
        health_amount = 9
        return health_amount

    def attack(self):
        attack_amount = randint(2,7)
        return attack_amount


class Rat(Monster):

    def health(self):
        health_amount = 5
        return health_amount

    def attack(self):
        attack_amount =  randint(1,3)
        return attack_amount


class Wizard(Monster):

    def health(self):
        health_amount = 15
        return health_amount

    def attack(self):
        attack_amount = randint(3,10)
        return attack_amount


class Slime(Monster):

    def health(self):
        health_amount = 7
        return health_amount

    def attack(Self):
        attack_amount = randint(2,5)
        return attack


class Boss(Monster):

    def health(self):
        health_amount = 20
        return health_amount

    def attack(self):
        attack_amount = randint(5,15)
        return attack_amount

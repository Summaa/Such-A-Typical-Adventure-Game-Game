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

        potions = self
        potions = 0
        return potions


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
        return attack_amount


class Boss(Monster):

    def health(self):
        health_amount = 30
        return health_amount

    def attack(self):
        attack_amount = randint(5,15)
        return attack_amount

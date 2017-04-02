from sys import exit
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

    def inventory(self):
        pass


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


class TestFight(object):

    def __init__(self):
        pass

    def enter(self):
        print "This is a test for a combat system."
        print "Type fight."

        button = raw_input("> ")

        if button.lower() == "fight":
            print "Fighting."

            boss_health = Boss().health()
            player_health = Player().health()

            while boss_health > 0:
                player_attack = Player().attack()

                print "What is your action?"

                action = raw_input("> ")

                if action.lower() == "attack":
                    print "You go move in to stab for %s damage." % player_attack
                    boss_health = boss_health - player_attack
                    print "The boss slashes back in a mad rage."
                    player_health = player_health - Boss().attack()
                    print "The boss now has %s health." % boss_health
                    print "You now have %s health." % player_health

                elif action.lower() == "exit":
                    exit(1)

                if boss_health <= 0:
                    print "You killed the boss congrats!"



test_fight = TestFight()
test_fight.enter()

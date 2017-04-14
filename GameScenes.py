from GameCharacters import Player, Goblin, Rat, Wizard, Slime, Boss

player_health = Player().health()
potions = Player().potions()

class Scene(object):

    def enter(self):

        """This sets what will happen when the scene is called and will be
           inherited and changed by all child Scenes.
        """
        print "This scene is not yet configured."
        exit(1)


class Death(Scene):

    def enter(self):
        print "Looks like you've died. Gotta try harder if you want to beat"
        print "this typical adventure!"
        print "Do you want to continue? Y/N"

        answer = raw_input("> ")

        if answer.lower() == "y":
            return 'throne_room'

        else:
            exit(1)


class ThroneRoom(Scene):

    def enter(self):
        print "Room name."
        room_name = raw_input("> ")
        return '%s' % room_name

        print "BAM! With a flash of light you suddenly find yourself inside the"
        print "body of an average built man with an average face."
        print "You very quickly realise that you have been brought into a very"
        print "typical adventure scenario. Of course with any typical adventure"
        print "story you have to get a quest and where better to get a quest"
        print "than the throne room you happen to be in. It now dawns on you"
        print "that this whole time an old man has been blabing at you and"
        print "you've been too busy with how typical this scenario is to"
        print "notice. As the old man comes into focus you see a crown on top"
        print "of his head. \"Of course! How typical, get a quest from a king.\""
        print "You think to yourself. You finally start to pay attention to"
        print "what the king is saying and hear \"So there you have it my dear"
        print "adventurer, I lost my crown in the Dungeon of Doom and I'm too"
        print "old and frail to get it. Will you help me?\" Now since this is"
        print "a typical adventure game (game) you have absolutely no choice"
        print "but to say yes. With that the king gives a jolly old laugh and"
        print "motions for the guard to usher you out and lead you to the"
        print "entrance of the Dungeon of Doom."

        return 'dungeon_entrance'


class DungeonEntrance(Scene):

    def enter(self):
        raw_input("Press enter to continue > ")

        print "Hours pass on your journey to the Dugeon of Doom and the"
        print "atmosphere is tense while following the guard. You ask the guard"
        print "what you could expect from the dungeon. \"I can't say. Nobody"
        print "has made it past the entrance and only a few have even made it"
        print "back from there.\" He responds. You begin to sweat upon hearing"
        print "that news and proceed to prod further asking why no one has "
        print "made it past the entrance. The guard sighs and says \"A riddle.\""
        print "\"A riddle?\" You ask. \"Yes and apparently the hardest in all"
        print "the realms. We've had grand scholars accompany the toughest of"
        print "adventurers and they have been unable to solve it. From the"
        print "stories I've heard if you get it wrong a rock guardian will slay"
        print "you.\" You shake you head wondering how you, a typical"
        print "adventurer, are expected to get into a dungeon where the even the"
        print "best couldn't get past the entrance. Just as you are about to"
        print "state your doubts the guard abruptly halts and points to a"
        print "mountain a short distance away. \"That is the entrance to the"
        print "dungeon and hear is where I must leave you on your own. I wish"
        print "you the best of luck adventurer\" With that the guard tips his"
        print "head to you and proceeds to start running back to the kings"
        print "village. It seems no matter what doubts you have you going in"
        print "one way or another."

        raw_input("Press enter to continue > ")

        print "As you approach the mountain and what looks to you like a"
        print "plausible hidden entrance you begin to feel a strong vibration"
        print "from the ground. In front of you, you begin to see a face form"
        print "out of the mountain side. It looks much like an old scholarly"
        print "man with a big rocky beard. Suddenly the eyes on the face open"
        print "and the entire face begins to animate. It looks to you and begins"
        print "to speak with a deep booming vocie. \"Welcome young hero!\""
        print "Much to your suprise this rock face is speaking to you and"
        print "apparently knows you intentions without you saying anything."
        print "You quickly realise this must be the rock guardian. Obviously"
        print "reading your mind the guardian begins to speak again. \"Yes"
        print "I know why your here hero. Eons of being a guardian of this place"
        print "has left me learning many arcane secrets such as how to read"
        print "minds, a dark practice lost a millennium ago.\" The guardian"
        print "begins to gurmble as he speaks again. \"Well hero as you already"
        print "know you must solve a riddle given by me, though what was lost"
        print "in the rumors you were told is that I'm quite forgiving and will"
        print "give you three tries to get the right answer. You must know"
        print "once you agree and I ask the riddle there is no going back."
        print "You must solve it, or die.\" You gulp at the last part of what"
        print "the guardian said. The rock continues and asks \"So hero what"
        print "will it be, do you think you have the smarts? Not a single"
        print "person, even the brightest of their time knew the answer to this"
        print "riddle.\" You swallow deeply again know you have no choice and"
        print "begin to speak the word yes as you are interrupted by the rock."
        print "\"Good! Then let us begin shall we?\""

        raw_input("Press enter to continue > ")

        print "\"There once was a king who had no sons, no daughters, and no"
        print "queen. For that reason he had to decide who would take the throne"
        print "after he dies. To do this he decided that he would give all of"
        print "the children of the kingdom a single seed. Whichever child had"
        print "the largest, most beautiful plant would earn the throne; this"
        print "being a metaphor for the kingdom. At the end of the contest all"
        print "of the children came to the palace with their enormous and"
        print "beautiful plants in hand. After he looked at all of the"
        print "children's pots, he finally decided that the little girl with an"
        print "empty pot would be the next Queen. Why did he choose this little"
        print "girl over all of the other children with their beautiful plants?\""

        answer = raw_input("> ")
        tries = 0
        true_answer  = "the king gave them all fake seeds and the little girl was the only honest child who didn't switch seeds."

        while tries < 2 and answer.lower() != true_answer:
            tries += 1
            print "\"No hero, that is not the answer I am looking for."
            print "That is try number %s.\" the guardian replies." % tries
            answer = raw_input("> ")

        if tries <= 2 and answer.lower() == true_answer:
            print "The rock guardian lets out a loud laugh that shake the"
            print "land around you. \"Very good young hero! In all my years"
            print "I never thought a young adventurer like yourself would"
            print "be the one to crack me open.\" As the guardian finishes"
            print "his sentence his face begins to turn back into the normal"
            print "rock face. You then hear a loud cha-chunk and see the"
            print "spot where the guardians face was turn into a door that"
            print "slowly creaks open inviting you in. With a sigh of relief"
            print "you proceed to walk into the dugeon. You ready your blade"
            print "wondering what's in store for you as you walk into the"
            print "darkness."

            raw_input("Press enter to continue > ")

            return 'goblin_room_1'

        elif tries == 2 and answer.lower() != true_answer:
            print "The guardian give you a stern look and says \"Well hero"
            print "it appears you have used all your tries.\" His voice"
            print "deepens considerably and the ground around you shakes"
            print "as the guardian begins to grow a enourmous rock body"
            print "and climbs off of the mountain. The guardian now"
            print "towering over proceeds to yell \" Now you must die!\""
            print "With a giant swing of his adult tree sized arm the "
            print "guardian proceeds to crush you killing you instantly."

            return 'death'


class GoblinRoom1(Scene):

    def enter(self):
        print "You soon come across a part of the dungeon that is well lit by"
        print "torches. This looks to you like the first chamber of this"
        print "dungeon. As you look around for a way forward you  hear the sound"
        print "of rocks breaking and a quick pitter patter of feet walking"
        print "behind you. You turn around to see nothing but continue to hear"
        print "shallow breathing around you. Suddenly a harsh voice screams out"
        print "out at you \"You shouldn't be hear huuu-man. Turn back now or"
        print "suffer my wrath!\" After a quick gulp you reply \"I'm hear to"
        print "get the kings crown, I cannot turn around!\" You hear a hiss and"
        print "the voice says \"Very well. Then prepare yourself!\" At that you"
        print "see something jump out of the shadows at you and as it comes"
        print "closer you can make out the figure of... a goblin! You realise"
        print "that while it may be feirce looking it is very small in stature"
        print "and not very well armed. It is equiped with rags and a single"
        print "iron dagger. You ready yourself for what looks like a fight."

        goblin_health = Goblin().health()
        global player_health

        while goblin_health > 0:
            player_attack = Player().attack()
            goblin_attack = Goblin().attack()

            print "You currently have %s health." % player_health
            print "The goblin currently has %s health." % goblin_health
            print "What is your action?"

            action = raw_input("> ")
            player_action = False

            if action.lower() == "attack" and player_action == False:
                print "You lunge forward giving a satisfying stab for %s damage." % player_attack
                goblin_health = goblin_health - player_attack
                print "The goblin now has %s health." % goblin_health
                player_action = True

            if player_action == True and player_health > 0 and goblin_health > 0:
                print "The goblin retaliates with a quick slash of his own for %s damage." % goblin_attack
                player_health = player_health - goblin_attack
                print "You now have %s health." % player_health
                player_action = False

            if player_health <= 0:
                print "You fall to your knees after the last attack from the"
                print "goblin to weak to stand again. The goblin begins to"
                print "laugh and starts to slowly walk to you. It gives a"
                print "creepy smile that sends a chill down your spine and says"
                print "\"Well huuu-man I warned you didn't I? Now you will"
                print "become a feast for my children.\" With that the goblin"
                print "finally reaches you and gives you one last solid hit on"
                print "you head knocking you out."
                print "You are soon brought to the goblins home and cooked for"
                print "its family to eat and never wake up again."

                return 'death'

            if goblin_health <= 0:
                print "With your last stab the goblin falls to his knees giving"
                print "one more loud hiss at you before you end him. Now that"
                print "goblin is out of the way you take a moment to recover and"
                print "decide to move on. Looking around you see three possible"
                print "directions to go to. You can go to your left, you can go"
                print "forward, or you can go to your right."
                print "What do you do?"

                while True:

                    action = raw_input("> ")

                    if "left" in action.lower():
                        print "You proceed to go to your left."

                        raw_input("Press enter to continue > ")

                        return 'item_room_1'

                    elif "forward" in action.lower():
                        print "You proceed to go forward."

                        raw_input("Press enter to continue > ")

                        return 'wizard_room'

                    elif "right" in action.lower():
                        print "You proceed to go to your right."

                        raw_input("Press enter to continue > ")

                        return 'rat_room'

                    else:
                        print "That is not a valid direction hero."

            else:
                print "That is not a valid action hero."


class ItemRoom1(Scene):

    def enter(self):
        global potions

        print "You enter the next room which looks the same as the one you just"
        print "came from, except this one has small chest in the center of it."
        print "You being cautious for a trap hesitantly tip toe towards the"
        print "chest. Once you are in front of it you raise you sword in front"
        print "of you and slowly begin to unlock the chest and open it. Inside"
        print "you see the chest has cushioning along the inner walls and within"
        print "that is a small glass bottle containing a red liquid. Picking up"
        print "the bottle and giving it a swish you feel that the liquid is a"
        print "little thicker than water which make you realise what you have."
        print "You picked up a healing potion! You quickly stow it away in your"
        print "item pouch for use whenever you want."
        potions += 1
        print "You now have %s healing potion." % potions

        raw_input("Press enter to continue > ")

        print "You look around a bit more and soon find out that the only thing"
        print "in this room was the healing potion and decide to move on."
        print "From this room you can only go forward and so forward you go."
        return 'slime_room'


class WizardRoom(Scene):

    def enter(self):
        print "As you move through the passage way further into the dungeon you"
        print "come across a strange wall of fog that blocks your path."
        print "You tentatively go up to the wall and try to touch it."
        print "As you reach out your hand glides through the fog with ease."
        print "What ever this thing is it appears you can move through it with-"
        print "-out a problem. So with that discovery in mind you step forward"
        print "to make your way through the fog."

        raw_input("Press enter to continue > ")

        print "After only a couple of steps the thick fog is gone and you find"
        print "yourself in what looks like a castle tower. You notice the floor"
        print "has changed into wooden boards and the walls are now stone bricks"
        print "with the occasional hole that acts as a window."
        print "All around the inside of this room are giant towering bookshelves"
        print "full of books from top to bottom. You also hear a faint"
        print "bubbling sound coming from the back of the room. You decide that"
        print "the fog wall must of been some kind of portal and this must be"
        print "the home of the creator of portal. You ready yourself and head"
        print "to the back of the room."

        raw_input("Press enter to continue > ")

        print "As you round the corner of the wall of bookshelves you see just"
        print "what you expected for an occurance as strange as this, a wizard."
        print "Before you is a wise looking old man in a blue robe with star"
        print "shapes scattered across it. He has a long face full of wrinkles"
        print "and a very large grey beard that stretches down to the middle of"
        print "his chest. It appears his is mixing some potions and that is the"
        print "source of the bubbling sound that you heard before."
        print "As you begin to approach him he smiles and gives a small \"hmmm.\""
        print "Hearing him speak you immediately stop and look at him."
        print "He stops the mixing he was doing and sets down his book, then"
        print "looks at you in way that makes you think he is sizing you up."
        print "He then gets up from the chair he was sat on and starts to"
        print "address you. \"Welcome to my home hero! In all my years I have"
        print "never seen another human in this dungeon. You see I am the only"
        print "human to ever make it in here, well that is... before you came"
        print "along.\" He gives a senile laugh and continues. \"I came here"
        print "long ago, so long in fact, that it was forgotten to history that"
        print "I came here and instead it was said I died in the great war that"
        print "was going on at the time. What really happened was that I came"
        print "here looking for arcane secrets to help bring the already long"
        print "conflict to a conclusion. I did accomplish my goal but at the"
        print "cost of being trapped hear. You see I found a great beast from"
        print "ancient times. I challenged the beast and was defeated."
        print "However the beast spared me and offered to share its arcane"
        print "secrets in exchange for my life and servitude in this dungeon."
        print "So I've been here ever since, kept alive by time lost magic and"
        print "a craving for knowledge.\" He clears his throat and continues."

        raw_input("Press enter to continue > ")

        print "\"And now here you are, bringing me back to reality. I believe it"
        print "is time for me to move on. So I am going to offer you assistance"
        print "hero, but you must prove yourself to me by showing me that you"
        print "know your history, for it is that skill that will help you fight"
        print "the beast at the end of your journey. If you fail you must prove"
        print "yourself in combat, if you fail that then I will end your journey"
        print "here since if you can not beat me you will no doubt loose to the"
        print "ancient beast. Of course you could always skip the test of the"
        print "mind and go strait for the test of the body with a fight to the"
        print "death, it is up to you hero."
        print "So what do you say hero, which test will you take now?\""

        while True:

            answer = raw_input("> ")

            if "mind" in answer.lower():
                print "The old wizard smiles and proceeds to say \"Very well hero, I"
                print "shall give you a simple question and a good chance to get it"
                print "right. I will give you four possible answers and allow you to"
                print "have two chances at getting the right answer. After that if"
                print "you don't get the right answer we will move on to the test"
                print "of the body. If you get it right I will grant you a gift to"
                print "assist you on your journey through the dungeon.\" He pauses"
                print "to take a deep breath before going on. \"Now for your"
                print "question, a test of your knowledge of history."
                print "What... is my name?"
                print "I was a famous great wizard of my time, all you need to do is"
                print "know which one I was and get my name. As for your possible"
                print "answers, my name is one of the following. Merlin, Gandalf,"
                print "Dumbledore, or Atlantes.\""
                print "\"So... who am I?\""

                tries = 0

                while tries != 2:

                    answer = raw_input("> ")

                    if answer.lower() == "Merlin" and tries != 2:
                        print "\"That is correct! Very good hero!"
                        print "Now as promised, I will assist you on you journey."
                        print "Tell me, did you notice anything strange about"
                        print "that fog that you passed through to get here?\""
                        print "Before you can answer Merlin goes on to explain."
                        print "\"If you guessed it was a portal, you would be"
                        print "correct! What I am going to do for you, is send"
                        print "you forth into the depths of the dungeon with"
                        print "this portal. That is, I'm going to put you in"
                        print "the room right before the beast of this dungeon"
                        print "so you do not have to waste your energy fighting"
                        print "the pesky monsters strewn about this place."
                        print "Once you go through you will not be able to come"
                        print "back, but you will find yourself in a room that"
                        print "contains one of my healing potions to help beat"
                        print "the beast.\" As he finishes Merlin snaps his"
                        print "fingers and you see the portal change color"
                        print "slightly. \"Now go forth hero, and rid this"
                        print "world of the horrid dungeon.\" With that he"
                        print "beckons you to the portal. You give him a quick"
                        print "thanks and goodbye and proceed to go through the"
                        print "portal."

                        raw_input("Press enter to continue > ")

                        return 'item_room_2'

                    else:
                        print "\"I'm sorry hero, but that is not my name.\""
                        tries += 1
                        print "That means you have %s tries left hero." % (2 - tries)

                    if tries == 2:
                        print "\"Well hero, it looks like you don't know enough to"
                        print "pass the test of the mind. Now prepare yourself for"
                        print "a fight to the death!"

                        raw_input("Press enter to continue > ")

                        return 'wizard_room_combat'

            elif "body" in answer.lower():
                print "\"Very well hero, than prepare yourself for a fight to the"
                print "death!\""

                raw_input("Press enter to continue > ")

                return 'wizard_room_combat'

            else:
                print "That is not a valid answer hero."


class WizardRoomCombat(Scene):

    def enter(self):
        print "You quickly bring up your sword and ready yourself for combat."

        raw_input("Press enter to continue > ")

        wizard_health = Wizard().health()
        global player_health

        while wizard_health > 0:
            player_attack = Player().attack()
            wizard_attack = Wizard().attack()

            print "You currently have %s health." % player_health
            print "Merlin currently has %s health." % wizard_health
            print "What is your action?"

            action = raw_input("> ")
            player_action = False

            if action.lower() == "attack" and player_action == False:
                print "You move fast going for a hard slash for %s damage." % player_attack
                wizard_health = wizard_health - player_attack
                print "Merlin now has %s health." % wizard_health
                player_action = True

            if player_action == True and player_health > 0 and wizard_health > 0:
                print "Merlin retaliates with a magic missle for %s damage." % wizard_attack
                player_health = player_health - wizard_attack
                print "You now have %s health." % player_health
                player_action = False

            if player_health <= 0:
                print "You fall to your knees after the last attack from Merlin"
                print "He looks at you breathing heavily and says \"Well hero I"
                print "commend you for giving it your all but it looks like your"
                print "all wasn't enough. I'll end your suffering now and wish"
                print "you good travel to the after-life.\" With that Merlin"
                print "casts another spell this time summoning a sword."
                print "With a quick wave of his hand the sword proceeds to come"
                print "at you, stabbing you through the heart and ending your"
                print "life."

                return 'death'

            if wizard_health <= 0:
                print "After you last attack Merlin ceases to fight, only"
                print "standing and holding his chest wound. Coughing blood"
                print "every few words he says \"Well, well, well hero it looks"
                print "like you might have what it take to go head to head with"
                print "the beast after all. I only wish you would of passed the"
                print "test of the mind so I could of lent you some assistance."
                print "Oh well at least I can rest easy now knowing there is"
                print "hope to have this dungeon destroyed.\" Sighing his last"
                print "breath his whispers \"Good luck hero.\" and falls to the"
                print "ground dead."

                raw_input("Press enter to continue > ")

                print "After composing yourself for a moment, you decide to move"
                print "on. Seeing no other way to go, you proceed to go back"
                print "through the portal that brought you here."

                raw_input("Press enter to continue > ")

                return 'returned_goblin_room_1'


class ReturnedGoblinRoom1(Scene):

    def enter(self):
        print "As you pass through the portal you find yourself in the exact"
        print "same spot as before you met Merlin. You continue on, returning"
        print "to the chamber where you fought the goblin, its body still there"
        print "untouched. You stand back at the spot where you first made the"
        print "decision on which direction to go facing the same way as well."
        print "You now know that going forward is useless, thus leaving you"
        print "with two options, left or right."
        print "Which way do you go?"

        while True:

            answer = raw_input("> ")

            if "left" in answer.lower():
                print "You proceed to go left."

                raw_input("Press enter to continue > ")

                return 'item_room_1'

            elif "right" in answer.lower():
                print "You proceed to go right."

                raw_input("Press enter to continue > ")

                return 'rat_room'


class RatRoom(Scene):

    def enter(self):
        print "After a few minutes of walking in this direction you come to a"
        print "solid stone wall with a hand print on it. You put you hand on"
        print "hand print and the wall glides upwards letting you into the next"
        print "chamber. You look ahead before entering and see what looks like"
        print "a fluffy ball moving around in the center of the dimly lit"
        print "chamber. You also hear faint squeaks coming from the ball of"
        print  "fur. You decide to raise your sword and enter the room."

        raw_input("Press enter to continue > ")

        print "The moment you clear the stone wall it closes shut behind you"
        print "giving you no chance to react. The ball of fur immediately turns"
        print "and looks at you, from this distance you can make out the shape"
        print "of the creature and to you it looks like it is a small rat."
        print "You take another step forward and the rat lets out a terrifying"
        print "screech stopping you in your tracks. Next thing you know the"
        print "rats eyes start to glow red and its body begins to shake"
        print "violently. Before your very eyes the rat begins to grow in size."
        print "Not believing what you are seeing you close your eyes and rub"
        print "them. When you open your eyes you see a rat the size of a large"
        print "dog. Again the rat lets out a large screech, then begins to"
        print "charge at you. You shake yourself out of your disbelief and"
        print "take a fighting stance."

        raw_input("Press enter to continue > ")

        rat_health = Rat().health()
        global player_health

        while rat_health > 0:
            player_attack = Player().attack()
            rat_attack = Rat().attack()

            print "You currently have %s health." % player_health
            print "The rat currently has %s health." % rat_health
            print "What is your action?"

            action = raw_input("> ")
            player_action = False

            if action.lower() == "attack" and player_action == False:
                print "You lunge forward giving a satisfying stab for %s damage." % player_attack
                rat_health = rat_health - player_attack
                print "The rat now has %s health." % rat_health
                player_action = True

            if player_action == True and player_health > 0 and rat_health > 0:
                print "The rat lets out a harsh sound and bites you for %s damage." % rat_attack
                player_health = player_health - rat_attack
                print "You now have %s health." % player_health
                player_action = False

            if player_health <= 0:
                print "After the last bite you feel your strength wane and you"
                print "fall flat on the ground exausted. With a few short"
                print "squeaks which sound to you like gloating, the rat jumps"
                print "on your body and begins to eat you alive. You spend the"
                print "next and last hour of your life in agony as the rat eats"
                print "you."

                return 'death'

            if rat_health <= 0:
                print "After your last lunge the rat falls on its side beaten."
                print "Barely breathing you end the rats pain with a final stab"
                print "through its heart. Successful in your fight you take a"
                print "moment to catch you breath before moving on. Once you"
                print "feel ready you give the chamber you are in a good look"
                print "around and come to the conclusion that the only way is"
                print "forward. Taking one more deep breath you step off"
                print "towards what will surely be another challenge."

                raw_input("Press enter to continue > ")

                return 'goblin_room_2'


class SlimeRoom(Scene):

    def enter(self):
        # Add potions from here on (Skip goblin room 2).
        pass


class GoblinRoom2(Scene):

    def enter(self):
        pass


class ItemRoom2(Scene):

    def enter(self):
        pass


class BossRoom(Scene):

    def enter(self):
        pass


class TreasureRoom(Scene):

    def enter(self):
        pass


class Map(object):

    scenes = {
        'death': Death(),
        'throne_room': ThroneRoom(),
        'dungeon_entrance' : DungeonEntrance(),
        'goblin_room_1': GoblinRoom1(),
        'item_room_1': ItemRoom1(),
        'wizard_room': WizardRoom(),
        'wizard_room_combat': WizardRoomCombat(),
        'returned_goblin_room_1': ReturnedGoblinRoom1(),
        'rat_room': RatRoom(),
        'slime_room': SlimeRoom(),
        'goblin_room_2': GoblinRoom2(),
        'item_room_2': ItemRoom2(),
        'boss_room': BossRoom(),
        'treasure_room': TreasureRoom()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

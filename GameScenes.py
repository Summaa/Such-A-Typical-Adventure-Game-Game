

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
        pass


class ItemRoom1(Scene):

    def enter(self):
        pass


class WizardRoom(Scene):

    def enter(self):
        pass


class RatRoom(Scene):

    def enter(self):
        pass


class SlimeRoom(Scene):

    def enter(self):
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

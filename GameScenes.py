

class Scene(object):

    def enter(self):

        """This sets what will happen when the scene is called and will be
           inherited and changed by all child Scenes.
        """
        print "This scene is not yet configured."
        exit(1)


class Death(Scene):

    def enter(self):
        pass


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
        pass


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
        'throne_room': ThroneRoom()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

from GameCharacters import Player, Boss

class Scene(object):

    def enter(self):

        """This sets what will happen when the scene is called and will be
           inherited and changed by all child Scenes.
        """
        pass


class Death(Scene):

    def enter(self):
        pass


class ThroneRoom(Scene):

    def enter(self):
        pass


class DungeonEntrance(Scene):

    def enter(self):
        pass


class DungeonRoom1(Scene):

    def enter(self):
        pass


class ItemRoom1(Scene):

    def enter(self):
        pass


class DungeonRoom2(Scene):

    def enter(self):
        pass


class DungeonRoom3(Scene):

    def enter(self):
        pass


class DungeonRoom4(Scene):

    def enter(self):
        pass


class DungeonRoom5(Scene):

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

    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

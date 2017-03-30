from GameScenes import ThroneRoom, DungeonEntrance, GoblinRoom1, ItemRoom1
from GameScenes import WizardRoom, RatRoom, SlimeRoom,GoblinRoom2
from GameScenes import ItemRoom2, BossRoom, TreasureRoom, Map, Scene

class Engine(object):

    def  __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):

        """Used to run the games Scenes."""

        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('treasure_room')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

a_map = Map('throne_room')
game = Engine(a_map)
game.play()

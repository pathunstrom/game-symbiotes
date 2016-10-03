import logging

from pygame.sprite import LayeredDirty

from symbiotes.levels import Scene, Map
from symbiotes.sprites import Player


class FightTheReaper(Scene):

    def __init__(self):
        logging.getLogger(__name__).debug("Create Reaper Fight")
        super().__init__()
        self.map = Map((1000, 1000))
        Player(self.player)
        self.boss = LayeredDirty()

    def update(self, time_delta):
        self.player.update(time_delta)

    def render(self):
        pass

    def handle_event(self, event):
        pass
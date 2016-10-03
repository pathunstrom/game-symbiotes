import logging

from pygame.rect import Rect
from pygame.sprite import DirtySprite
from pygame.surface import Surface


class Player(DirtySprite):

    def __init__(self, map, *groups):
        super().__init__(*groups)
        logging.getLogger(__name__).debug("Player created.")
        self.x = 0  # TODO: VECTORS!
        self.y = 0
        self.map = map
        self.image = Surface((20, 20))
        self.rect = Rect(0, 0, 20, 20)
        self.image.fill((255, 0, 0))
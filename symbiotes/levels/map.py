from pygame import Rect


class Map(object):

    def __init__(self, size, origin=(0, 0)):
        self.limits = Rect((0, 0), size)  # for bounds collision
        self.origin = origin

    def contains(self, sprite):

        sprite_rect = sprite.rect.move(*self.origin)

        if not self.limits.contains(sprite_rect):
            return False, self
        else:
            return True, None


# TODO: Good place to implement quad trees
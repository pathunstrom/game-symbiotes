import logging

from pygame import display, sprite
import pygame

TIME_DELTA = 1000/60


class Scene(object):
    player = sprite.GroupSingle()
    world = sprite.LayeredDirty()
    display_surface = display.get_surface()
    clock = pygame.time.Clock()

    def __init__(self):
        self.accumulated_time = 0
        self.unused_time = 0

    def run(self):
        while self.running:
            self._handle_events()
            self._update()
            self._render()

    def _handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            else:
                self.handle_event(event)
        logger = logging.getLogger(__name__)
        logger.debug("_handle_events count: {}".format(len(events)))

    def handle_event(self, event):
        raise NotImplementedError

    def _update(self):
        tick = self.clock.tick()
        self.unused_time += tick
        self.accumulated_time += tick
        logger = logging.getLogger(__name__)
        while self.unused_time >= TIME_DELTA:
            logger.debug("_update.unused_time: {}".format(self.unused_time))
            self.update(TIME_DELTA)
            self.unused_time -= TIME_DELTA

        logger.debug("_update.accumulated_time: {}".format(self.accumulated_time))

    def update(self, time_delta):
        raise NotImplementedError

    def _render(self):
        display.update(self.render())
        logger = logging.getLogger(__name__)
        logger.debug("_render")

    def render(self):
        raise NotImplementedError

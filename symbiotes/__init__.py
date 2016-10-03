import logging

import pygame

logging.basicConfig(level=logging.DEBUG)

pygame.init()

pygame.display.set_mode([800, 600])

logging.getLogger(__name__).info(pygame.display.Info())
logging.getLogger(__name__).info(pygame.display.list_modes())
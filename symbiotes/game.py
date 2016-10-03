import logging

import pygame

from symbiotes.levels import Village

logging.getLogger(__name__).debug("Symbiotes activated.")

Village().run()

pygame.quit()

import logging

from symbiotes.levels import Scene


class Village(Scene):

    def __init__(self):
        logging.getLogger(__name__).debug("Create village.")
        super().__init__()
        self.running = True


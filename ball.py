from pico2d import *
import game_world
import game_framework
import random

import server


class Ball:
    image = None

    def __init__(self, x=None, y=None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)

    def draw(self):
        sw = self.x - server.background.window_left
        sh = self.y - server.background.window_bottom
        self.image.draw(sw, sh)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        sw = self.x - server.background.window_left
        sh = self.y - server.background.window_bottom
        return sw - 10, sh - 10, sw + 10, sh + 10

    def handle_collision(self, group, other):
        if group == 'boy:balls':
            game_world.remove_object(self)

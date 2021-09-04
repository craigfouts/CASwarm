import matplotlib.animation as animation
import matplotlib.pyplot as plt
from typing import Iterable


class Swarm:

    def __init__(self, grid, controller):
        self.grid = grid
        self.controller = controller

    def run(self):
        fig, ax = plt.subplots(self.figsize)
        anim = animation.FuncAnimation(fig, )

    def save(fmt='.gif'):
        pass


class Controller:

    def __init__(self, grid):
        self.grid = grid

    def perceive():
        pass

    def update():
        pass

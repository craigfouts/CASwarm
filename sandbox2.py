from typing import Iterable
import matplotlib.pyplot as plt


class Swarm:

    def __init__(self, grid, controller, frames=100, interval=500, 
        figsize=(6, 6), save=None):
        assert frames >= 0
        assert interval > 0
        assert isinstance(figsize, Iterable)
        assert len(figsize) == 2

        self.grid = grid
        self.controller = controller
        self.frames = frames
        self.interval = interval
        self.figsize = figsize
        self.save = save

    def run(self):
        fig, ax = plt.subplots(self.figsize)

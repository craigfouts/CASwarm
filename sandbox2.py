import matplotlib.animation as animation
import matplotlib.pyplot as plt
from IPython.display import HTML


class Swarm:

    def __init__(self, grid, controller):
        self.grid = grid
        self.controller = controller(grid)

    def run(self):
        fig, ax = plt.subplots(6, 6)
        anim = animation.FuncAnimation(fig,
                                       self.controller.update,
                                       fargs=(self.grid, ax),
                                       frames=100,
                                       interval=500,
                                       blit=True)
        return HTML(anim.to_jshtml())

    def save(self, fname, fmt='.gif') -> None:
        fig, ax = plt.subplots(6, 6)
        anim = animation.FuncAnimation(fig,
                                       self.controller.update,
                                       fargs=(self.grid, ax),
                                       frames=100,
                                       interval=500,
                                       blit=True)
        anim.save(fname + fmt, writer=animation.PillowWriter(fps=2))


class Controller:

    def __init__(self, grid):
        self.grid = grid

    def update(i):
        pass

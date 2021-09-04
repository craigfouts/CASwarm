import numpy as np
from sandbox2 import Controller, Swarm


class GameOfLife(Controller):

    def __init__(self, grid):
        super().__init__(grid)

    def update(i, x, ax):
        ax.clear()
        ax.set_axis_off()
        y = np.zeros(shape=x.shape)
        for idx, _ in np.ndenumerate(x):
            n = 0
            for x_shift, y_shift in zip([-1,  0,  1, -1,  1, -1,  0,  1],
                                        [1,  1,  1,  0,  0, -1, -1, -1]):
                target = ((idx[0] + x_shift) % x.shape[1],
                          (idx[1] + y_shift) % x.shape[0])
                if x[target] > 0:
                    n += 1
            if (x[idx] == 1 and n in (2, 3)) or (x[idx] == 0 and n == 3):
                y[idx] = 1
        x[:, :] = y[:, :]
        return ax.imshow(x, cmap='binary'),


if __name__ == '__main__':
    x = np.array([[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    swarm = Swarm(grid=x, controller=GameOfLife)
    swarm.save(fname='animation')

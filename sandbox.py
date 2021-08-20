import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML


def update(i, x, ax):
    ax.clear()
    ax.set_axis_off()
    if i > 0:
        y = np.zeros(shape=x.shape)
        for idx, _ in np.ndenumerate(x):
            n = 0
            for x_shift, y_shift in zip([-1,  0,  1, -1,  1, -1,  0,  1],
                                        [ 1,  1,  1,  0,  0, -1, -1, -1]):
                target = ((idx[0] + x_shift) % x.shape[1],
                          (idx[1] + y_shift) % x.shape[0])
                if x[target] > 0:
                    n += 1
            if (x[idx] == 1 and n in (2, 3)) or (x[idx] == 0 and n == 3):
                y[idx] = 1
        x[:, :] = y[:, :]
    return ax.imshow(x, cmap='binary'),


def create_animation(update, x, figsize=(6, 6), frames=100, interval=500, save=None):
    fig, ax = plt.subplots(figsize=figsize)
    anim = animation.FuncAnimation(fig, update,
                                   fargs=(x, ax), frames=frames,
                                   interval=interval, blit=True)
    if save:
        anim.save(save, writer=animation.PillowWriter(fps=2))
    return HTML(anim.to_jshtml())


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
    create_animation(update, x, save='animation.gif')

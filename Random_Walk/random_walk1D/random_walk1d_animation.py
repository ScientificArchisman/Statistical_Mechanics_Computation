import numpy as np
import matplotlib.pyplot as plt
plt.style.use(["science", "notebook", "grid"])
import matplotlib.animation as animation

"""The strategy remains the same as the original randomwalk.ipynb, but now we use 
the animation module to animate the random walk using  a few random walkers."""

# Constants
N_STEPS = 1000 # Number of steps in each walk
N_WALKERS = 20 # Number of walkers
STEP_SIZE = .01 # Size of each step
START_POSITION = 0 # Initial position


def random_walk_1D(n_steps:int, n_walks:int, x0:int, step_size:float) -> np.ndarray:
    """Returns a 2D array of random walks
    Args:
        n_steps (int): Number of steps in each walk
        n_walks (int): Number of walks
        x0 (int): Initial position
        step_size (float): Size of each step
    Returns:
        walks(np.ndarray): 2D array of random walks"""
    # Create array of random steps
    steps = np.random.choice([-step_size, step_size], size=(n_walks, n_steps))
    # Create array of random walks
    walks = np.cumsum(steps, axis=1)
    walks  = np.insert(walks, 0, x0, axis=1) # Insert initial position
    return walks # Return the walks


def animate_walks(walks:np.ndarray, n_steps:int) -> None:
    """Animates the random walks
    Args:
        walks (np.ndarray): 2D array of random walks
        n_steps (int): Number of steps in each walk
    Returns:
        None"""
    
    n_walkers = walks.shape[0] # Number of walkers
    n_ypos = np.arange(-n_walkers//2, n_walkers//2) # y positions of the walkers

    # Create figure and axis
    fig, ax = plt.subplots(1, figsize=(8, 6))

    # Set axis labels
    ax.set_xlabel("Steps")
    ax.set_ylabel("Position")

    # Create empty lines
    lines = [ax.plot([0], ypos, "o")[0] for _, ypos in zip(range(n_walkers),
                                                                n_ypos)]
                                                                

    def animate(frame):
        """Update the lines in the animation"""
        # Set axis limits
        ax.set_xlim(walks.min(), walks.max())

        for (i, line), ypos in zip(enumerate(lines), n_ypos):
            x_arr = walks[i]
            line.set_xdata(x_arr[frame])
            line.set_ydata(ypos)
        return lines
    ax.set_title(f"Random Walk 1D, {STEP_SIZE=}, {N_WALKERS=}, {N_STEPS=}")
    
    # Create animation
    path_name = "/Users/archismanchakraborti/Desktop/python files/Jupyter_notebooks/computational lab/Stat_Mech/Random_Walk/random_walk1d_animation.gif"
    anim = animation.FuncAnimation(fig, animate, frames=n_steps, interval=10, blit=True)
    anim.save(path_name, writer="imagemagick", fps=60)


if __name__ == "__main__":
    walks = random_walk_1D(N_STEPS, N_WALKERS, START_POSITION, STEP_SIZE)
    animate_walks(walks, N_STEPS)


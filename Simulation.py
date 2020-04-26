import sys
import random
from Percolation import Percolation


def simulation(grid_size):
    P = Percolation(grid_size)
    while True:
        row = random.randint(1, grid_size)
        col = random.randint(1, grid_size)
        P.open_site(row, col)
        if P.percolates():
            p_est = P.n_of_open() / (grid_size**2)
            return p_est


def run_sim(grid_size, n_trials=1):
    result_list = []
    for i in range(n_trials):
        result_list.append(simulation(grid_size))
    m = sum(result_list) / len(result_list)
    s = (sum((x - m)**2 for x in result_list) / len(result_list)) ** 0.5
    print(f'Mean: {m} Stddev: {s}')


if __name__ == "__main__":
    arg = sys.argv[1:]
    if len(arg) != 2:
        sys.exit("Grid size and number of trials are required")
    else:
        run_sim(int(arg[0]), int(arg[1]))

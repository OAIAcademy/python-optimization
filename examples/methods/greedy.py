import numpy as np

from examples.problems import knapsack


def greedy():
    value_ratio = np.copy(knapsack.values / knapsack.weight)
    sol = np.zeros(knapsack.SIZE)
    func = lambda x: 1 if x else 0
    while True:
        too_big = knapsack.weight > (knapsack.CAPACITY - (sol * knapsack.weight).sum())
        for i in range(0, too_big.size):
            if too_big[i]:\
                value_ratio[i] = 0
        if value_ratio.sum() == 0:
            return knapsack.score(sol), sol
        p = value_ratio.argmax()
        sol[p] = 1
        value_ratio[p] = 0


if __name__ == '__main__':
    print(greedy())

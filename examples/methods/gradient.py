import random

random.seed(0)

import time

from examples.problems import knapsack, travelling_salesman


def gradient(start, neigh, score):
    best = score(start)
    sol = start
    while True:
        yield score(sol), sol
        sol = min([(score(i), i) for i in neigh(sol)], key=lambda x: x[0])[1]
        if best < score(sol):
            yield score(sol), sol
            break
        else:
            best = score(sol)


if __name__ == '__main__':

    print("Knapsack")
    t = time.time()
    for score, sol in gradient(knapsack.random_solution(), knapsack.all_neighbourhood, knapsack.score):
        print(score)
        if time.time() - t >= 10:
            break
    print("salesman")
    t = time.time()
    for score, sol in gradient(travelling_salesman.random_solution(), travelling_salesman.all_neighbourhood,
                               travelling_salesman.score):
        print(score)
        if time.time() - t >= 10:
            break

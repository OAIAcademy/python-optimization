import random

random.seed(0)

import time

from examples.problems import knapsack, travelling_salesman


def tabu(start, neigh, score, max_time):
    tabu_list = set()
    best = start
    sol = start
    t = time.time()
    while True:
        if time.time() - t >= 5:
            break
        new_sol = min([(score(i), i) for i in neigh(sol) if tuple(i) not in tabu_list], key=lambda x: x[0])[1]
        tabu_list.add(tuple(new_sol))
        if len(tabu_list) > 10000:
            tabu_list.remove(random.choice(tuple(tabu_list)))
        if score(new_sol) < score(best):
            best = new_sol
            yield score(best), best
        sol = new_sol


if __name__ == '__main__':

    print("Knapsack")

    for score, sol in tabu(knapsack.random_solution(), knapsack.all_neighbourhood, knapsack.score, max_time=5):
        print(score)

    print("salesman")

    for score, sol in tabu(travelling_salesman.random_solution(), travelling_salesman.all_neighbourhood,
                           travelling_salesman.score, max_time=3):
        print(score)

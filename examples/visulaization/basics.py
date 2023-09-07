import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from examples.methods.gradient import gradient
from examples.methods.stochastic_gradient import stochastics_gradient
from examples.methods.tabu import tabu
from examples.methods.annealing import anealing
from examples.methods.particle_swarm import particle_swarm
from examples.methods.genetic import genetic
from examples.problems import knapsack

results = {}
results["gradient"] = pd.Series(
    [i[0] for i in gradient(knapsack.random_solution(), knapsack.all_neighbourhood, knapsack.score)],
)
results["stochastics"] = pd.Series(
    [i[0] for i in stochastics_gradient(knapsack.random_solution(), knapsack.mutation, knapsack.score)],
)
results["tabu"] = pd.Series(
    [i[0] for i in tabu(knapsack.random_solution(), knapsack.all_neighbourhood, knapsack.score, 10)],
)
results["anealing"] = pd.Series(
    [i[0] for i in anealing(knapsack.random_solution(), knapsack.mutation, knapsack.score, 10)],
)
results["particle_swarm"] = pd.Series(
    [i[0] for i in particle_swarm(knapsack.random_solution, knapsack.mutation, knapsack.score, 10)],
)
results["genetic"] = pd.Series(
    [i[0] for i in genetic(knapsack.random_solution, knapsack.mutation, knapsack.hybrid, knapsack.score, 10)],
)

pd.DataFrame(results).plot()
plt.show()
pd.DataFrame(results).plot(ylim=[None, 0])
plt.show()
pd.DataFrame(results).plot(ylim=[-2500, -2000])
plt.show()
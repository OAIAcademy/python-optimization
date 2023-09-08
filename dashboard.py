import numpy as np
from matplotlib import pyplot as plt
from examples.methods.genetic import genetic
from examples.methods.particle_swarm import particle_swarm
from examples.problems import knapsack
import streamlit as st

max_time = int(st.text_input("max time"))
pop_size = int(st.text_input("pop size"))
method = st.selectbox("Method", ["Genetic", "Swarm"])

data = []
if method == "Genetic":
    results = [i[0] for i in
               genetic(knapsack.random_solution, knapsack.mutation, knapsack.hybrid, knapsack.score, max_time, pop_size,
                       data)]
else:
    results = [i[0] for i in
               particle_swarm(knapsack.random_solution, knapsack.mutation, knapsack.score, max_time, pop_size, data)]

averages = np.array([i[0].mean() for i in data])
deviation = np.array([i[0].std() for i in data])
avg_sol = [sum([sol for sol in pop[1]]) / len(pop[1]) for pop in data]
affinity = [np.mean(np.abs(avg_sol[i] - 0.5)) for i in range(len(avg_sol))]

fig, ax = plt.subplots()
ax.plot(results)
ax.set_title('Best score')
st.pyplot(fig)

fig, ax = plt.subplots()
ax.plot(averages - np.min(averages) + 1)
ax.set_yscale('log')
ax.set_title('Avarage pop score')
st.pyplot(fig)

fig, ax = plt.subplots()
ax.plot(deviation)
ax.set_title('Pop score std')
st.pyplot(fig)

fig, ax = plt.subplots()
ax.plot(affinity)
ax.set_title('Pop affinity')
st.pyplot(fig)

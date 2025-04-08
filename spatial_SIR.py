import numpy as np
import matplotlib.pyplot as plt
# import necessary libraries
beta = 0.3  # infection probability
gamma = 0.05  # recovery probability
# set model parameters
population = np.zeros((100, 100))
# make array of all susceptible population
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1
# select an initial infection point randomly
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title("Initial State (Time = 0)")
plt.colorbar()
plt.show()
# draw the initial state
for time in range(100): # simulate 100 time steps
    new_population = population.copy()
    # create a copy of the current state for update
    infected_indices = np.where(population == 1)
    infected_coords = list(zip(infected_indices[0], infected_indices[1]))
    # obtain the coordinates of all infected individuals
    for i, j in infected_coords: # process each infected individual
        for di in [-1, 0, 1]: # infect 8 neighbors
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue  # skip himself
                ni, nj = i + di, j + dj
                if 0 <= ni < 100 and 0 <= nj < 100: # check the boundaries
                    if population[ni, nj] == 0 and np.random.random() < beta:
                        new_population[ni, nj] = 1
                    # if the neighbor is susceptible, infect with probability beta
        if np.random.random() < gamma:
            new_population[i, j] = 2
        # the infected individual recovers with probability gamma
    population = new_population # update the overall state
    # draw the state at key time points
    if time in [9, 49, 99]:  # correspond to the 10th, 50th, and 100th steps (counting from 0)
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f"Time = {time+1}")
        plt.colorbar()
        plt.show()
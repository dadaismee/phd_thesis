import numpy as np

# Define the payoff matrix for the IPD
payoff_matrix = np.array([[3, 0], [5, 1]])

# Define the initial population with all players defecting
population = np.zeros((n, 2), dtype=int)

# Define the initial delta parameter
delta = 0.1

# Define the function for updating the population and delta


def update(population, delta):
    n = population.shape[0]
    new_population = np.zeros_like(population)

    # Loop over all pairs of players
    for i in range(n):
        for j in range(i+1, n):
            # Determine the strategy of each player based on their previous actions
            if i == 0:
                # First round: both players defect
                action_i, action_j = 0, 0
            else:
                # Subsequent rounds: use the tit-for-tat strategy
                last_action_j = population[j, i-1]
                action_i = last_action_j
                action_j = last_action_i

            # Update the payoffs based on the chosen strategies
            payoff_i, payoff_j = payoff_matrix[action_i,
                                               action_j], payoff_matrix[action_j, action_i]

            # Update the population based on the payoffs and delta parameter
            if payoff_i > payoff_j:
                new_population[i, i] += 1
                new_population[i, j] += 1
                if payoff_j - payoff_i > delta:
                    delta += 0.01
            elif payoff_j > payoff_i:
                new_population[j, j] += 1
                new_population[j, i] += 1
                if payoff_i - payoff_j > delta:
                    delta += 0.01

    # Normalize the population to get the proportions of each strategy
    population = new_population / (2 * n)

    return population, delta


# Run the simulation for a certain number of rounds
n_rounds = 100
for i in range(n_rounds):
    population, delta = update(population, delta)

# Print the final population and delta parameter
print("Final population:")
print(population)
print("Final delta parameter: ", delta)

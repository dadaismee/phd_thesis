import numpy as np
import matplotlib.pyplot as plt

# set up the game parameters
V = 20  # value of the disputed resource
C = 5   # cost of fighting

# define the payoff matrix
payoff_matrix = np.array([[V/2, V-C], [0, V/2-C]])

# define the strategies for Hawk and Dove
HAWK = 0
DOVE = 1

# define a function to play the game iteratively
def play_game(strategy_1, strategy_2, rounds):
    # initialize scores to zero
    score_1 = 0
    score_2 = 0
    
    # play the game for specified number of rounds
    for i in range(rounds):
        # determine actions based on strategies
        if strategy_1 == HAWK:
            if strategy_2 == HAWK:
                score_1 += payoff_matrix[0][0]
                score_2 += payoff_matrix[0][0]
            else:
                score_1 += payoff_matrix[0][1]
                score_2 += payoff_matrix[1][0]
        else:
            if strategy_2 == HAWK:
                score_1 += payoff_matrix[1][0]
                score_2 += payoff_matrix[0][1]
            else:
                score_1 += payoff_matrix[1][1]
                score_2 += payoff_matrix[1][1]

    return (score_1, score_2)

# define a function to simulate games between two populations with different proportions of Hawk and Dove players
def simulate_game(population_a_hawk_prop, population_b_hawk_prop, rounds_per_game):
    # initialize scores to zero
    a_score = 0
    b_score = 0
    
    # determine number of players in each population based on proportions and total population size of 10000
    num_a_hawks = int(population_a_hawk_prop * 10000)
    num_b_hawks = int(population_b_hawk_prop * 10000)
    
    # determine number of Dove players in each population 
    num_a_doves = 10000 - num_a_hawks 
    num_b_doves = 10000 - num_b_hawks
    
     # play games between pairs of randomly selected players from each population 
     #(with replacement) and accumulate scores over all games played 
     #(num_games is set to twice the total population size)
    
    for i in range(20000): 
        a_player_strategy = np.random.choice([HAWK, DOVE], p=[population_a_hawk_prop, (1-population_a_hawk_prop)])
        b_player_strategy = np.random.choice([HAWK, DOVE], p=[population_b_hawk_prop, (1-population_b_hawk_prop)])
        
        results_tuple=play_game(a_player_strategy,b_player_strategy,rounds_per_game)
        
        a_score+=results_tuple[0]     
        b_score+=results_tuple[1]  
        
    return (a_score,b_score)

# define a function that plots a chart showing how total scores between two populations vary with changes in proportion of hawkish players in one population 

def plot_population_proportions_varying_scores(rounds_per_game):
    
   
   x_values=[]
   y_values=[]
   
   for i in range(11):
      
      x_values.append(i/10)
      y_values.append(simulate_game(i/10,(10-i)/10,rounds_per_game))
      
   
   plt.plot(x_values,[x[0]for x in y_values ],label='Population A Score')
   plt.plot(x_values,[x[1]for x in y_values ],label='Population B Score')
   
   plt.xlabel('Proportion of Hawkish Players In Population A')
   plt.ylabel('Total Score')
   
   plt.title('Scores For Different Proportions Of Hawkish Players In Population A(N={})'.format(rounds_per_game))
  
   plt.legend()
  
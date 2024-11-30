import numpy as np
from matplotlib import pyplot as plt

import probability


def print_ruined_plot(turns: [int], results: [float], prob: float) -> None:
    x_axis = np.array(turns)
    y_axis = np.array(results)

    plt.plot(x_axis, y_axis)
    plt.title("Simulation for probability of A winning a round: " + str(prob))
    plt.xlabel('Amount of turns')
    plt.ylabel('Probability of any player being ruined')
    plt.show()


if __name__ == '__main__':
    game_experiments = 500

    stakes = [50, 50]
    prob_a_arr = [0.2, 0.5, 0.8]

    turns_limit = 1000
    turns_arr = []
    prob_turn_results = []

    for prob_a in prob_a_arr:
        for turn in range(1, turns_limit):
            turns_arr.append(turn)
            ruined_prob = probability.any_ruined_within_turns(prob_a,
                                                              game_experiments,
                                                              stakes,
                                                              turn)
            prob_turn_results.append(ruined_prob)

        print_ruined_plot(turns_arr, prob_turn_results, prob_a)
        turns_arr.clear()
        prob_turn_results.clear()

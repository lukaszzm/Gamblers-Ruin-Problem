from typing import Any

import numpy as np
from matplotlib import pyplot as plt
from numpy import floating

import game
import probability


def print_ruined_plot(turns: [int], results: [float], prob: float) -> None:
    x_axis = np.array(turns)
    y_axis = np.array(results)

    plt.plot(x_axis, y_axis)
    plt.title("Simulation for probability of A winning a round: " + str(prob))
    plt.xlabel('Amount of turns')
    plt.ylabel('Probability of any player being ruined')
    plt.show()


def mean_turns_to_ruin(probability_value: float, experiments: int, stakes_arr: [int]) -> \
        floating[Any]:
    ruined_turns_arr = []

    for i in range(1, experiments):
        results = game.play_game(stakes_arr, probability_value)
        last_result = results[max(results)]
        turns = len(results)

        if len(results) == game.MAX_ROUNDS:
            experiments = max(1, experiments - 1)
        elif game.is_player_ruined(last_result, 0) or game.is_player_ruined(last_result,
                                                                            1):
            ruined_turns_arr.append(turns)

    return np.mean(ruined_turns_arr)


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

        mean_result = mean_turns_to_ruin(prob_a, game_experiments, stakes)
        print(f"Mean turns to ruin for probability {prob_a}: {int(mean_result)} turns")

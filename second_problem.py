import numpy as np
from matplotlib import pyplot as plt

import analytical
import game


def ruined_a_probability(probability: float, rounds: int, experiments: int,
                         initial_stakes: [int, int]) -> float:
    ruined = 0

    for j in range(1, experiments):
        results = game.play_game(initial_stakes, probability, rounds)
        last_result = results[max(results)]
        if game.is_player_ruined(last_result, 0):
            ruined += 1

    return ruined / experiments


def problem_plot(stake_arr: [float], results: [float], title: str) -> None:
    x_axis = np.array(stake_arr)
    y_axis = np.array(results)

    plt.plot(x_axis, y_axis)
    plt.title(title)
    plt.xlabel('Amount of stake A')
    plt.ylabel('Probability of A being ruined')
    plt.show()


if __name__ == '__main__':
    game_rounds = 100
    game_experiments = 1000

    stakes_sum = 100
    prob_a = 0.5

    prob_results = []
    analytical_results = []
    stakes_arr = []

    for k in range(1, stakes_sum):
        stake_a = k
        stakes = [stake_a, stakes_sum - stake_a]
        stakes_arr.append(stake_a)

        prob_result = ruined_a_probability(prob_a, game_rounds,
                                           game_experiments, stakes)
        prob_results.append(prob_result)

        analytical_result = analytical.solution(prob_a, stakes)
        analytical_results.append(analytical_result)

    problem_plot(stakes_arr, prob_results, "Simulation")
    problem_plot(stakes_arr, analytical_results, "Analytical")

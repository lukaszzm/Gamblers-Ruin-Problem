import numpy as np
from matplotlib import pyplot as plt

import game


def any_ruined_probability(probability: float, rounds: int, experiments: int,
                           initial_stakes: [int, int]) -> [float, [int]]:
    ruined = 0
    after_arr = []

    for j in range(1, experiments):
        results = game.play_game(initial_stakes, probability, rounds)
        last_result = results[max(results)]

        if game.is_player_ruined(last_result, 0) or game.is_player_ruined(last_result, 1):
            ruined += 1
            after_arr.append(len(results))

    return [ruined / experiments, after_arr]


def average_turns(turns: [int]) -> float:
    return sum(turns) / len(turns)


def print_ruined_plot(turns: [int], results: [float], title: str) -> None:
    x_axis = np.array(turns)
    y_axis = np.array(results)

    plt.plot(x_axis, y_axis)
    plt.title(title)
    plt.xlabel('Amount of turns')
    plt.ylabel('Probability of any player being ruined')
    plt.show()


def print_average_turns_plost(average: [float], turns: [float], title: str) -> None:
    x_axis = np.array(turns)
    y_axis = np.array(average)

    plt.plot(x_axis, y_axis)
    plt.title(title)
    plt.xlabel('Amount of turns')
    plt.ylabel('Average amount of turns until a player is ruined')
    plt.show()


if __name__ == '__main__':
    game_rounds = 100
    game_experiments = 1000

    stakes = [50, 50]
    prob_a_arr = [0.2, 0.5, 0.8]

    turns_limit = 100

    turns_arr = []
    prob_turn_results = []
    average_arr = []

    for prob_a in prob_a_arr:
        for k in range(1, turns_limit):
            turns_arr.append(k)
            [prob_turn, ruined_after_arr] = any_ruined_probability(prob_a, k,
                                                                   game_experiments,
                                                                   stakes)
            if len(ruined_after_arr) > 0:
                average_arr.append([k, average_turns(ruined_after_arr)])

            prob_turn_results.append(prob_turn)

        print_ruined_plot(turns_arr, prob_turn_results,
                          "Simulation for probability of A winning a round: " + str(
                              prob_a))

        print_average_turns_plost([x[1] for x in average_arr],
                                  [x[0] for x in average_arr],
                                  "Average amount of turns until a player is ruined for "
                                  "probability of A winning a round: " + str(
                                      prob_a))

        turns_arr.clear()
        prob_turn_results.clear()
        average_arr.clear()

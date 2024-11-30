import matplotlib.pyplot as plt
import numpy as np

import analytical
import probability


def problem_plot(prob_arr: [float], results: [float], title: str) -> None:
    x_axis = np.array(prob_arr)
    y_axis = np.array(results)

    plt.plot(x_axis, y_axis)
    plt.title(title)
    plt.xlabel('Probability of A winning a round')
    plt.ylabel('Probability of A being ruined')
    plt.show()


if __name__ == '__main__':
    game_experiments = 1_000
    stakes = [50, 50]

    prob_results = []
    analytical_results = []
    prob_a_arr = []

    for k in range(1, 100):
        prob_a = k / 100
        prob_a_arr.append(prob_a)

        prob_result = probability.ruined_player(prob_a,
                                                game_experiments,
                                                0, stakes)
        prob_results.append(prob_result)

        analytical_result = analytical.solution(prob_a, stakes)
        analytical_results.append(analytical_result)

    problem_plot(prob_a_arr, prob_results, "Simulation")
    problem_plot(prob_a_arr, analytical_results, "Analytical")

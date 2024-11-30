import numpy as np
from matplotlib import pyplot as plt

import game


def game_trajectory(init_stakes: [int], probability: float) -> (
        [int], [int]):
    current_stake = init_stakes[0]
    win_count = 0
    wins_arr = []
    turns_arr = []

    game_results = game.play_game(init_stakes, probability)

    if len(game_results) == game.MAX_ROUNDS:
        raise ValueError("Game is not finished, try again with more rounds")

    for turn, result in game_results.items():
        stake_after = result[0]

        if stake_after > current_stake:
            win_count += 1

        current_stake = stake_after
        turns_arr.append(turn + 1)
        wins_arr.append(win_count)

    return wins_arr, turns_arr


def trajectory_plot(trajectories: [([int], [int])], probabilities: [float]) -> None:
    if len(trajectories) != len(probabilities):
        raise ValueError(
            "Trajectory array and probability array must have the same length")

    max_turns = 0

    for trajectory, prob in zip(trajectories, probabilities):
        wins, turns = trajectory

        x_axis = np.array(turns)
        y_axis = np.array(wins)

        max_turns = max(max(turns), max_turns)

        plt.plot(x_axis, y_axis, drawstyle = "steps-pre",
                 label = f"Game trajectory with {prob} probability")

    plt.xticks(range(0, max_turns))
    plt.yticks(range(0, max_turns))
    plt.legend()
    plt.xlabel('Turns')
    plt.ylabel('Wins')
    plt.show()


def print_results(trajectory: ([int], [int]), prob: float) -> None:
    wins, turns = trajectory

    print(f"Game trajectory with {prob} probability")
    print(f"Turns: {max(turns)}")
    print(f"Player A wins: {max(wins)}")
    print("-----------------------------")


if __name__ == '__main__':
    stakes = [50, 50]
    prob_a_arr = [0.2, 0.5, 0.8]
    trajectory_results_arr = []

    for prob_a in prob_a_arr:
        trajectory_result = game_trajectory(stakes, prob_a)
        print_results(trajectory_result, prob_a)
        trajectory_results_arr.append(trajectory_result)

    trajectory_plot(trajectory_results_arr, prob_a_arr)

import numpy as np
from matplotlib import pyplot as plt

import game


def get_game_trajectory(init_stakes: [int], probability: float, rounds: int) -> (
        [int], [int]):
    current_stake = init_stakes[0]
    win_count = 0
    wins_arr = []
    turns_arr = []

    game_results = game.play_game(stakes, probability, rounds)

    for turn, result in game_results.items():
        stake_after = result[0]

        if stake_after > current_stake:
            win_count += 1

        current_stake = stake_after
        turns_arr.append(turn + 1)
        wins_arr.append(win_count)

    return wins_arr, turns_arr


def trajectory_plot(trajectory: [(int, int, str)]) -> None:
    for wins_result, turns_result, label in trajectory:
        x_axis = np.array(turns_result)
        y_axis = np.array(wins_result)
        plt.plot(x_axis, y_axis, drawstyle = "steps-pre",
                 label = f"Game trajectory with {label}")
        plt.xticks(range(0, len(turns)))
        plt.yticks(range(0, len(turns)))

    plt.title("Game trajectories")
    plt.legend()
    plt.xlabel('Turns')
    plt.ylabel('Wins')
    plt.show()


if __name__ == '__main__':
    game_rounds = 10
    stakes = [50, 50]
    prob_a_arr = [0.2, 0.5, 0.8]

    trajectories_arr = []

    for prob_a in prob_a_arr:
        wins, turns = get_game_trajectory(stakes, prob_a, game_rounds)
        trajectories_arr.append((wins, turns, f"prob_a = {prob_a}"))

    trajectory_plot(trajectories_arr)

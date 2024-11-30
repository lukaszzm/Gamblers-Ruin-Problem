import random

MAX_ROUNDS = 100_000
STAKE = 1


def is_player_ruined(player_values: [int, int], player_index: int = 0) -> bool:
    return player_values[player_index] <= 0


def play_turn(player_values: [int, int], a_prob: float, stake: int = 1) -> [int, int]:
    random_value = random.random()
    return [player_values[0] + stake, player_values[1] - stake] \
        if random_value < a_prob \
        else [player_values[0] - stake, player_values[1] + stake]


def play_game(player_values: [int, int], a_prob: float, max_rounds: int = MAX_ROUNDS,
              stake: int = STAKE) -> dict[int, [int, int]]:
    results = {}

    for i in range(max_rounds):
        player_values = play_turn(player_values, a_prob, stake)
        results[i] = player_values
        if is_player_ruined(player_values, 0) or is_player_ruined(player_values, 1):
            break

    return results

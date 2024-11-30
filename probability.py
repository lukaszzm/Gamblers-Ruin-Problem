import game


def ruined_player(probability: float,
                  experiments: int,
                  player_index: int,
                  initial_stakes: [int, int]
                  ) -> float:
    ruined = 0

    for j in range(1, experiments):
        results = game.play_game(initial_stakes, probability)
        last_result = results[max(results)]

        if len(results) == game.MAX_ROUNDS:
            experiments = max(1, experiments - 1)
        elif game.is_player_ruined(last_result, player_index):
            ruined += 1

    return ruined / experiments


def any_ruined(probability: float,
               experiments: int,
               initial_stakes: [int, int]
               ) -> float:
    ruined = 0

    for j in range(1, experiments):
        results = game.play_game(initial_stakes, probability)
        last_result = results[max(results)]

        if len(results) == game.MAX_ROUNDS:
            experiments = max(1, experiments - 1)
        elif game.is_player_ruined(last_result, 0) or game.is_player_ruined(last_result,
                                                                            1):
            ruined += 1

    return ruined / experiments


def any_ruined_within_turns(probability: float,
                            experiments: int,
                            initial_stakes: [int, int],
                            turns: int
                            ) -> float:
    ruined = 0

    for j in range(1, experiments):
        results = game.play_game(initial_stakes, probability, turns)
        last_result = results[max(results)]

        if len(results) == game.MAX_ROUNDS:
            experiments = max(1, experiments - 1)
        elif game.is_player_ruined(last_result, 0) or game.is_player_ruined(last_result,
                                                                            1):
            ruined += 1

    return ruined / experiments

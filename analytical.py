def solution(probability: float, initial_stakes: [int, int]) -> float:
    p = probability
    q = 1 - p
    i = initial_stakes[0]
    m = sum(initial_stakes)

    result = i / m if p == q else (1 - (q / p) ** i) / (1 - (q / p) ** m)
    return 1 - result

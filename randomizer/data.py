from randomizer.generator import generate_board


def generate_classic():
    tiles = {"forest": 4, "pasture": 4, "field": 4, "hill": 3, "mountain": 3}
    rows = [3, 4, 5, 4, 3]
    total_tokens = {1: 1, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 8: 2, 9: 2, 10: 2, 11: 2, 12: 1}
    generated_tiles = [[], [], [], [], []]
    generated_tokens = [[], [], [], [], []]

    result = generate_board(tiles.copy(), rows.copy(), total_tokens.copy(), generated_tiles.copy(), generated_tokens.copy())

    return result


def generate_expanded():
    tiles = {"forest": 6, "pasture": 6, "field": 6, "hill": 5, "mountain": 5}
    rows = [3, 4, 5, 6, 5, 4, 3]
    total_tokens = {1: 2, 2: 2, 3: 3, 4: 3, 5: 3, 6: 3, 8: 3, 9: 3, 10: 3, 11: 3, 12: 2}
    generated_tiles = [[], [], [], [], [], [], []]
    generated_tokens = [[], [], [], [], [], [], []]

    result = generate_board(tiles.copy(), rows.copy(), total_tokens.copy(), generated_tiles.copy(), generated_tokens.copy())

    return result



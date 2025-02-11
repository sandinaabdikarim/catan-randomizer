from randomizer.generator import generate_board


def generate_classic():
    tiles = ["forest", "forest", "forest", "forest", "pasture", "pasture", "pasture", "pasture",
             "field", "field", "field", "field", "hill", "hill", "hill", "mountain", "mountain", "mountain"]
    rows = [3, 4, 5, 4, 3]
    total_tokens = [1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
    generated_tiles = [[], [], [], [], []]
    generated_tokens = [[], [], [], [], []]

    result = generate_board(tiles.copy(), rows.copy(), total_tokens.copy(), generated_tiles.copy(), generated_tokens.copy())

    return result


def generate_expanded():
    tiles = ["forest", "forest", "forest", "forest", "pasture", "pasture", "pasture", "pasture",
             "field", "field", "field", "field", "hill", "hill", "hill", "mountain", "mountain", "mountain",
             "forest", "forest", "pasture", "pasture", "field", "field", "hill", "hill", "mountain", "mountain"]
    rows = [3, 4, 5, 6, 5, 4, 3]
    total_tokens = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 8, 8, 8, 9, 9, 9, 10, 10, 10,
                    11, 11, 11, 12, 12]
    generated_tiles = [[], [], [], [], [], [], []]
    generated_tokens = [[], [], [], [], [], [], []]

    result = generate_board(tiles.copy(), rows.copy(), total_tokens.copy(), generated_tiles.copy(), generated_tokens.copy())

    return result



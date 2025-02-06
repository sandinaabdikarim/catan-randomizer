from random import randint, randrange


def checking_rules(prev_row, curr_num, prev_num, curr_num_idx):
    is_num_rules_ok = True

    if curr_num == prev_num:
        is_num_rules_ok = False
    elif (curr_num == 6 and prev_num == 8) or (curr_num == 8 and prev_num == 6):
        is_num_rules_ok = False
    elif curr_num in prev_row:
        for up_token in range(0, len(prev_row)):
            if curr_num_idx == up_token and curr_num == prev_row[up_token]:
                is_num_rules_ok = False
            elif curr_num_idx - up_token == 1 and curr_num == prev_row[up_token]:
                is_num_rules_ok = False
    elif curr_num in [6, 8]:
        for up_token in range(0, len(prev_row)):
            if (curr_num + prev_row[up_token] == 14) and (
                    curr_num_idx == up_token or curr_num_idx - up_token == 1):
                is_num_rules_ok = False
                break

    return is_num_rules_ok


def generate_tokens(rows, total_tokens):
    generated_tokens = [[], [], [], [], []]
    curr_token = 0
    prev_token = 0
    for row in range(len(rows)):
        for token in range(rows[row]):
            num_of_tries = 0
            is_token_rules_ok = False

            while not is_token_rules_ok and num_of_tries < len(total_tokens) * 3:
                curr_idx = randrange(0, len(total_tokens))
                curr_token = total_tokens[curr_idx]
                num_of_tries += 1

                is_token_rules_ok = checking_rules(generated_tokens[row - 1], curr_token, prev_token, token)
                if is_token_rules_ok:
                    break
                else:
                    continue

            if not is_token_rules_ok:
                return []

            generated_tokens[row].append(curr_token)
            prev_token = curr_token
            total_tokens.remove(curr_token)

    return generated_tokens

def generate_hexes(tiles, gen_numbers):
    generated_tiles = [[], [], [], [], []]

    for row in range(len(gen_numbers)):
        for token in range(len(gen_numbers[row])):
            if gen_numbers[row][token] == 1:
                generated_tiles[row].append("desert")
            else:
                ran_tile_num = randint(0, len(tiles) - 1)
                ran_tile = tiles[ran_tile_num]
                generated_tiles[row].append(ran_tile)
                tiles.remove(ran_tile)

    return generated_tiles

def generate_board():
    hexes = ["forest", "forest", "forest", "forest", "pasture", "pasture", "pasture", "pasture",
             "field", "field", "field", "field", "hill", "hill", "hill", "mountain", "mountain", "mountain"]
    total_rows = [3, 4, 5, 4, 3]
    number_tokens = [1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]

    is_success = False
    generated_tokens = []

    while not is_success:
        generated_tokens = generate_tokens(total_rows.copy(), number_tokens.copy())
        if len(generated_tokens) != 0:
            is_success = True

    generated_hexes = generate_hexes(hexes.copy(), generated_tokens)

    generated_board = ()

    for row in range(len(generated_hexes)):
        dict_for_tuple = ()
        for item in range(len(generated_hexes[row])):
            dict_for_tuple_row = {}
            dict_for_tuple_row[generated_hexes[row][item]] = generated_tokens[row][item]
            dict_for_tuple = dict_for_tuple + (dict_for_tuple_row,)

        generated_board = generated_board + (dict_for_tuple,)

    return generated_board


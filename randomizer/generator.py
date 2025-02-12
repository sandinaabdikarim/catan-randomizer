import copy
from random import randint, randrange


def checking_rules(prev_row, curr_num, prev_num, curr_num_idx):

    rules = {
        "same_numbers": lambda curr_num, prev_num: curr_num == prev_num,
        "six_or_eight": lambda curr_num, prev_num: (curr_num == 6 and prev_num == 8) or (
                    curr_num == 8 and prev_num == 6),
        "check_prev_row": lambda curr_num, prev_row, curr_num_idx: any(
            (
                    (curr_num_idx == up_token and curr_num == prev_row[up_token]) or
                    (abs(curr_num_idx - up_token) == 1 and curr_num == prev_row[up_token]) or
                    (curr_num + prev_row[up_token] == 14 and (
                                curr_num_idx == up_token or (abs(curr_num_idx - up_token) == 1)))
            ) for up_token in range(len(prev_row))
        )
    }

    is_num_rules_ok = True

    if any([
        rules["same_numbers"](curr_num, prev_num),
        rules["six_or_eight"](curr_num, prev_num),
        rules["check_prev_row"](curr_num, prev_row, curr_num_idx)
    ]):
        is_num_rules_ok = False

    return is_num_rules_ok


def generate_tokens(rows, total_tokens, gen_tokens):

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

                is_token_rules_ok = checking_rules(gen_tokens[row - 1], curr_token, prev_token, token)
                if is_token_rules_ok:
                    break
                else:
                    continue

            if not is_token_rules_ok:
                return []

            gen_tokens[row].append(curr_token)
            prev_token = curr_token
            total_tokens.remove(curr_token)

    return gen_tokens

def generate_hexes(tiles, gen_numbers, generated_tiles):

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

def generate_board(hexes, total_rows, number_tokens, gen_hexes, tokens):

    is_success = False
    generated_tokens = []

    while not is_success:
        copy_tokens = copy.deepcopy(tokens)
        generated_tokens = generate_tokens(total_rows.copy(), number_tokens.copy(), copy_tokens)
        if len(generated_tokens) != 0:
            is_success = True

    generated_hexes = generate_hexes(hexes.copy(), generated_tokens, gen_hexes)

    generated_board = ()

    for row in range(len(generated_hexes)):
        dict_for_tuple = ()
        for item in range(len(generated_hexes[row])):
            dict_for_tuple_row = {}
            dict_for_tuple_row[generated_hexes[row][item]] = generated_tokens[row][item]
            dict_for_tuple = dict_for_tuple + (dict_for_tuple_row,)

        generated_board = generated_board + (dict_for_tuple,)

    return generated_board


winning_list = [5, 17, 14]
guessed_list = [5, 14, 17]


def winning_numbers(winning_list, guessed_list):

    if guessed_list[0] in guessed_list:

        if guessed_list[1] in guessed_list:

            if guessed_list[2] in guessed_list:

                return "First"

        else:

            return "Second"

    else:

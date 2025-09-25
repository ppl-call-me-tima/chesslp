def get_file_from_phonetic(phonetic):
    return {
        "file": phonetic[0]
    }

def get_rank_value_from_number(number):
    if number == "one": return 1
    elif number == "two": return 2
    elif number == "three": return 3
    elif number == "four": return 4
    elif number == "five": return 5
    elif number == "six": return 6
    elif number == "seven": return 7
    elif number == "eight": return 8

def get_file_and_rank_from_algebraic(algebraic):
    return {
        "file": algebraic[0].lower(),
        "rank": int(algebraic[1])
    }

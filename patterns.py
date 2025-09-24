# pattern defintion
# move
piece_pattern = [
    [{"LOWER": "pawn"}],
    [{"LOWER": "knight"}],
    [{"LOWER": "bishop"}],
    [{"LOWER": "rook"}],
    [{"LOWER": "queen"}],
    [{"LOWER": "king"}],
]

phonetic_pattern = [
    [{"LOWER": "alpha"}],
    [{"LOWER": "bravo"}],
    [{"LOWER": "charlie"}],
    [{"LOWER": "delta"}],
    [{"LOWER": "echo"}],
    [{"LOWER": "foxtrot"}],
    [{"LOWER": "golf"}],
    [{"LOWER": "hotel"}],
]

number_pattern = [
    [{"LOWER": "one"}],
    [{"LOWER": "two"}],
    [{"LOWER": "three"}],
    [{"LOWER": "four"}],
    [{"LOWER": "five"}],
    [{"LOWER": "six"}],
    [{"LOWER": "seven"}],
    [{"LOWER": "eight"}],
]

move_pattern = [
    [{"LOWER": "play"}, {"LOWER": "the"}, {"LOWER": "move"}],
    [{"LOWER": "make"}, {"LOWER": "the"}, {"LOWER": "move"}],
]

# status
status_pattern = [
    [{"LOWER": "winning"}],
    [{"LOWER": "points"}],
    [{"LOWER": "evaluation"}],
    [{"LOWER": "position"}, {"LOWER": "status"}]
]

# best_move
best_move_pattern = [
    [{"LOWER": "best"}, {"LOWER": "move"}],
    [{"LOWER": "recommend"}, {"LOWER": "a"}, {"LOWER": "move"}]
]

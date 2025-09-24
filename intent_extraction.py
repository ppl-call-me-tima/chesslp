import spacy
from spacy.matcher import Matcher

from helpers import *

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

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

matcher.add("piece", piece_pattern)
matcher.add("phonetic", phonetic_pattern)
matcher.add("number", number_pattern)

matcher.add("make_move", move_pattern)
matcher.add("position_status", status_pattern)
matcher.add("best_move", best_move_pattern)

types_of_intents = {"make_move", "position_status", "best_move"}

# matching
def get_intent(text):
    doc = nlp(text)
    matches = matcher(doc)

    intentObj = {}

    if matches:
        for match_id, start, end in matches:

            match_type = nlp.vocab.strings[match_id]
            content = str(doc[start:end])

            if match_type in types_of_intents:
                intentObj["intent"] = match_type
            else:
                if "move" not in intentObj:
                    intentObj["move"] = {}
                
                if match_type == "piece":
                    intentObj["move"]["piece"] = content
                elif match_type == "phonetic":
                    intentObj["move"]["file"] = get_file_from_phonetic(content)
                elif match_type == "number":
                    intentObj["move"]["rank"] = get_rank_from_number(content)

    return intentObj

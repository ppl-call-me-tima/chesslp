import spacy
from spacy.matcher import Matcher

from patterns import *
from helpers import *

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

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

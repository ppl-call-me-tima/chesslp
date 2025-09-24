import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

# pattern defintion
move_pattern = [
        [{"LOWER": "play"}, {"LOWER": "the"}, {"LOWER": "move"}],
        [{"LOWER": "make"}, {"LOWER": "the"}, {"LOWER": "move"}],
]

status_pattern = [
    [{"LOWER": "winning"}],
    [{"LOWER": "points"}],
    [{"LOWER": "evaluation"}],
    [{"LOWER": "position"}, {"LOWER": "status"}]
]

best_move_pattern = [
    [{"LOWER": "best"}, {"LOWER": "move"}],
    [{"LOWER": "recommend"}, {"LOWER": "a"}, {"LOWER": "move"}]
]

matcher.add("make_move", move_pattern)
matcher.add("position_status", status_pattern)
matcher.add("best_move", best_move_pattern)


# matching
text = "Recommend a move to me"

def get_intent(text):
    doc = nlp(text)
    matches = matcher(doc)
    
    intent = None
    
    if matches:
        for match_id, start, end in matches:

            intent = nlp.vocab.strings[match_id]
            matched_span = doc[start:end]
            
            # print(f"For the text '{text}':")
            # print(f"  - Matched span: '{matched_span.text}'")
            # print(f"  - Detected Intent: '{intent}'")

    return intent

import json
from intent_extraction import get_intent

nat_lang = input("What do you want to do: ")
intent = get_intent(nat_lang)

print(json.dumps(intent, indent=4))

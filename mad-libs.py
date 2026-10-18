# Introduction Instructions



# User Input Variables

adjective1 = input("[1/23] Enter an indefinite article (a/an) + adjective: ") 
kingdom_name = input("[2/23] Enter a name for a kingdom: ")
knight_name = input("[3/23] Enter a name: ")
knight_title = input("[4/23] Enter an adjective: ")
adjective2 = input("[5/23] Enter an adjective: ")
noun1 = input("[6/23] Enter an indefinite article (a/an) + noun: ") 
noun2 = input("[7/23] Enter an indefinite article (a/an) + noun: ") 
noun3 = input("[8/23] Enter an indefinite article (a/an) + noun: ") 
noun4 = input("[9/23] Enter an indefinite article (a/an) + noun: ") 
number = input("[10/23] Enter any number (in word form): ")
plural_noun = input("[11/23] Enter a plural noun: ")
verb1 = input("[12/23] Enter a past tense verb: ")
object_adjective = input("[13/23] Enter an adjective: ")
object = input("[14/23] Enter an object: ")
length_of_time = input("[15/23] Enter a length of time: ")
beast = input("[16/23] Enter an animal: ")
beast_name = input("[17/23] Enter a name you would give to a pet: ")
body_part = input("[18/23] Enter a body part: ")
verb2 = input("[19/23] Enter a verb: ")
animal = input("[20/23] Enter an indefinite article (a/an) + animal: ")
verb3 = input("[21/23] Enter a past tense verb: ")
emotion = input("[22/23] Enter an emotion: ") # Doesn't work with words like "happy", "sad", "angry"
last_word = input("[23/23] Enter any word: ")


# Story 

story = print(f"\tThere once lived {adjective1.lower()} knight known throughout the kingdom of {kingdom_name.title()} as Sir\n"
              f"{knight_name.title()} the {knight_title.title()}. He had done many {adjective2.lower()} deeds in his time, which had\n"
              f"gotten him much recognition. He'd rescued {noun1.lower()} trapped in {noun2.lower()}, fought {noun3.lower()} with only\n"
              f"{noun4.lower()}, and once took on an army of {number.lower()} {plural_noun.lower()} on his own…and won. However, it\n"
              f"was his final quest that cemented him in the history of {kingdom_name.title()} forever.\n"
              f"\t Sir {knight_name.title()} {verb1.lower()} everywhere across the country in search of the {object_adjective.title()}\n"
              f"{object.title()}, an relic said to be able to bring the dead back to Earth and pull the living down to\n"
              f"Hell. {length_of_time.title()} before he'd embarked on his journey, the heir of {kingdom_name.title()} had tragically\n"
              f"died in an attack by the fearsome {beast.lower()} called {beast_name.title()}. The king had decreed, in his\n"
              f"mourning and desire for vengeance, that whoever brought the {body_part.title()} of {beast_name.title()} to\n"
              f"him as well as the {object_adjective.title()} {object.title()} would be granted a wish. Sir {knight_name.title()} had\n"
              f"dreamed of being able to {verb2.lower()} like {animal.lower()}. It had been this dream that willed him to\n"
              f"{kingdom_name.title()}, even as he suffered in anguish. When he reached the throne room, he fell\n"
              f"before the king. Both the {object_adjective.title()} {object.title()} and the {body_part.title()} of {beast_name.title()}\n"
              f"dropped from his hands. The king kneeled beside the fallen knight. He begged to\n"
              f"know what it was Sir {knight_name.title()} wished. Sir {knight_name.title()} whispered but one word before\n"
              f"he died of his flesh wounds. The King had {verb3.lower()} with {emotion.lower()} when he heard it, and echoed\n"
              f"it to all that witnessed the terrible scene. “{last_word.title()}”.")


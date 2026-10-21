# User Input Variables

adjective1 = input("[1/22] Enter an indefinite article (a/an) + adjective: ") 
kingdom_name = input("[2/22] Enter a name for a kingdom: ")
knight_name = input("[3/22] Enter a name: ")
knight_title = input("[4/22] Enter an adjective: ")
adjective2 = input("[5/22] Enter an adjective: ")
noun1 = input("[6/22] Enter an indefinite article (a/an) + noun: ") 
noun2 = input("[7/22] Enter an indefinite article (a/an) + noun: ") 
noun3 = input("[8/22] Enter an indefinite article (a/an) + noun: ") 
noun4 = input("[9/22] Enter an indefinite article (a/an) + noun: ") 
number = input("[10/22] Enter any number greater than 1: ")
plural_noun = input("[11/22] Enter a plural noun: ")
verb1 = input("[12/22] Enter a past tense verb: ")
object_adjective = input("[13/22] Enter an adjective: ")
object = input("[14/22] Enter an object: ")
length_of_time = input("[15/22] Enter a length of time: ")
beast = input("[16/22] Enter an animal: ")
beast_name = input("[17/22] Enter a name you would give to a pet: ")
body_part = input("[18/22] Enter a body part: ")
verb2 = input("[19/22] Enter a present tense verb: ")
verb2_2 = verb2.lower()
if verb2_2 == "ran":
    verb2_2 = "run" 
animal = input("[20/22] Enter an indefinite article (a/an) + animal: ")
verb3 = input("[21/22] Enter a past tense verb: ")
last_word = input("[22/22] Enter any word: ")


# Story 

story = print(f"\tThere once lived {adjective1.lower()} knight known throughout the kingdom of {kingdom_name.title()} as Sir\n"
              f"{knight_name.title()} the {knight_title.title()}. He had done many {adjective2.lower()} deeds in his time, which had\n"
              f"gotten him much recognition. He'd rescued {noun1.lower()} trapped in {noun2.lower()}, fought {noun3.lower()} with only\n"
              f"{noun4.lower()}, and once took on an army of {number.lower()} {plural_noun.lower()} on his own…and won. However, it\n"
              f"was his final quest that cemented him in the history of {kingdom_name.title()} forever.\n"
              f"\t Sir {knight_name.title()} {verb1.lower()} everywhere across the country in search of the {object_adjective.title()}\n"
              f"{object.title()}, a relic said to be able to rise one dead man from the Earth, and pull the man who resurected him down to\n"
              f"fill the grave. In which he would lie with the {object_adjective.title()} {object.title()} across his chest, until robbed\n"   
              f"of it by fate.\n" 
              f"\t{length_of_time.title()} before Sir {knight_name.title()} embarked on his journey, the heir of {kingdom_name.title()}\n"
              f"had tragically died in an attack by the fearsome {beast.lower()} called {beast_name.title()}. The king had decreed, in his\n"
              f"mourning and desire for vengeance, that whoever brought the {body_part.title()} of {beast_name.title()} to\n"
              f"him as well as the {object_adjective.title()} {object.title()} would be granted a wish. Sir {knight_name.title()} had\n"
              f"dreamed of being able to {verb2_2} like {animal.lower()}. It had been this dream that willed him to\n"
              f"{kingdom_name.title()}, even as he suffered in anguish.\n"
              f"\tWhen he reached the throne room, he fell before the king. Both the {object_adjective.title()} {object.title()}\n"
              f"and the {body_part.title()} of {beast_name.title()} dropped from his hands. The king knelt beside the fallen knight. \n"
              f"He begged to know what it was Sir {knight_name.title()} wished. Sir {knight_name.title()} whispered but one word before \n"
              f"he died of his flesh wounds. The King {verb3.lower()} when he heard it, and echoed it to all that witnessed the terrible scene.\n"
              f"“{last_word.title()}”.")


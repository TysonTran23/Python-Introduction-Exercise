

list = ["hello", "hey", "goodbye", "yo", "everything", "yes", "Evil"]
set_of_letters = {"h", "g", "y", "E"}
for word in list:
    word = word.upper()
    print(word)

def print_upper_words (list, set_of_letters):

    for word in list:
        for letter in word.split():
            for letter2 in set_of_letters:
                if letter.startswith(letter2):
                    print(word)

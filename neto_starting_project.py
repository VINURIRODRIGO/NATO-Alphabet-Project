import pandas
# TODO 1. Create a dictionary in this format:
while True:
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
    nato_dict = {row.letter: row.code for items, row in data.iterrows()}
    print(nato_dict)
    letters = [n for n in input("Enter a word: ")]
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

    try:
        print([nato_dict[letter.upper()] for letter in letters])
        break
    except KeyError:
        print("Sorry only letters in the alphabet please")

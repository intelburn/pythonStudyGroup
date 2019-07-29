import json
language = json.load(open("data.json", "r"))
#print(language)
word = input("Enter a word to search for: ")
if word in language.keys():
    print("The word {0} means:\n{1}".format(word, language[word]))
else:
    print("That is not a word in English")
import json
language = json.load(open("data.json", "r"))
word = input("Enter a word to search for: ")
if word in language.keys():
    print("The word {0} means:".format(word))
    for defination in language[word]:
        print(defination)
else:
    print("That is not a word in English")
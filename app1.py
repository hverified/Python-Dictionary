import json
from difflib import get_close_matches

# importing data into dictionary
raw_data = json.load(open("data.json"))

word = input("Enter the word: ")
# search word from the dictionary
def search_word(word):

    word = word.lower()

    if word in raw_data:
        return raw_data[word]

    elif word.title() in raw_data:
    	return raw_data[word.title()]

    elif word.upper() in raw_data:
    	return raw_data[word.upper()]

    elif len(get_close_matches(word, raw_data.keys()))>0:
        action = input("Did you mean %s instead? [y or n] " %get_close_matches(word, raw_data.keys())[0])
        if action == "y":
                return raw_data[get_close_matches(word, raw_data.keys())[0]]
        elif action == "n":
                return "Word doesn't exist!"
        else:
                return "Invalid Input !!!"
    else:
        return "Word doesn't exist in the dictionary"


output = search_word(word)

if type(output) == list:
    n = 1
    for i in output:
        print(n,"-",i)
        n+=1
else:
    print(output)

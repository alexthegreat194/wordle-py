import json
import pprint


url = '/usr/share/dict/words'
short_words = []
with open(url, 'r') as file:
    lines = file.readlines()
    for i, word in enumerate(lines):
        lines[i] = word.strip()
    
    for i, word in enumerate(lines):
        if len(word) is 5:
            short_words.append(word)

# print(short_words)

data = {
    'words': short_words
}

with open('wordle/words.json', 'w') as file:
    json_string = json.dumps(data)
    json.dump(data, file)

with open('wordle/words.json', 'r') as file:
    data = json.load(file)
    pprint.pprint(data)
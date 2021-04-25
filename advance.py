import json
import random
import terminal_banner

'''
structure :
    "A.D.": {
        "MEANINGS": {},
        "ANTONYMS": [],
        "SYNONYMS": []
    },
'''
## final variables
MEANINGS = 'MEANINGS'
ANTONYMS = 'ANTONYMS'
SYNONYMS = 'SYNONYMS'

def print_word_block(word_block):
    mean = word_block[MEANINGS]
    print('Meaning : ')
    for key in mean.keys() :
        ll = mean[key]
        print('\t' + ll[0] + ' :  ' + ll[1])


    print('Antonyms : ' + str(word_block[ANTONYMS]))
    print('Synonyms : ' + str(word_block[SYNONYMS]))


def meaning(word):
    word = word.upper()
    path_to_json_file = 'data/D{}.json'.format(word[0])
    data = json.load(open(path_to_json_file))
    word_block = data[word]
    print_word_block(word_block)
    

def random_picker():
    letter = random.randint(0, 26)
    data = json.load(open('data/D{}.json'.format( chr(letter+ord('A')) )))   
    words_pool = data.keys()
    picked_word = random.sample(words_pool, 1)[0]
    print(picked_word)
    print_word_block(data[picked_word])

def banner():
    banner_text = "Offline Dictionary.\n\nWith advance and vast data source.\
         \n\n from OBrutus http://github.com/obrutus"
    my_banner = terminal_banner.Banner(banner_text)
    print(my_banner)

if __name__ == '__main__':
    banner()
    word = input('Input the word : ')
    meaning(word)

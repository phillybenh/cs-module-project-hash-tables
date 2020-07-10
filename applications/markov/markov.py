import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# analyze which words can follow other words
s = words.split()
cache = {}
length = len(s)
for x in range(length):
    # s[(x+1+length) % length] wraps the last work around the the first word
    if s[x] not in cache:
        cache[s[x]] = [s[(x+1+length) % length]]
    else:
        cache[s[x]].append(s[(x+1+length) % length])
    # print(s[x])

# TODO: construct 5 random sentences
def sentence_constructor(dict):
    
    sentence_words = []
    sentence_length = 1
    stop_word = False

    def start_sentence(words):
        word = random.choice(list(words.keys()))
        if word[0] == '"':
            if word[1].isupper():
                return word
        elif word[0].isupper():
            return word
        else:
            return start_sentence(words)
    

    def is_stop_word(word):
        nonlocal stop_word
        stoppers = ['.', '?', '!']
        if word[-1] in stoppers:
           stop_word = True
           return stop_word
        elif word[-1] == '"' and word[-2] in stoppers:
            stop_word = True
            return stop_word
        else:
            return stop_word


    # start sentence with ranson start word
    current_word = start_sentence(cache)
    sentence_words.append(current_word)

    # using arbitrary 200 word sentance length maximum
    # in case some work combo exits that puts us in a inf. loop
    while stop_word is False and sentence_length < 2000:
        word = random.choice(cache[current_word])
        # print("***", cache[current_word])
        current_word = word
        sentence_words.append(current_word)
        sentence_length += 1
        is_stop_word(current_word)

    sentence_string = ' '.join([str(elem) for elem in sentence_words])
    return(sentence_string)


for i in range(5):
    print(sentence_constructor(cache))

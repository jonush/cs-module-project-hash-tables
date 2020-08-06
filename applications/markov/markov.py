import random
import string

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
def markov(words):
    d = {}

    words_list = words.split()

    # create a dictionary with each word as a key, and a empty list as the value
    for w in words_list:
        if w not in d:
            d[w] = []

    # if the key already exists, add the subsequent word into the list of values
    for i, w in enumerate(words_list):
        if i < len(words_list) - 1:
            d[w].append(words_list[i + 1])

    # create a list of words to form the sentence
    sentence = []
    # randomly select a key from the dictionary & append it to the sentence
    first = random.choice(list(d.keys()))
    sentence.append(first)
    # randomly select a word from the list of values and append it to the sentence
    next_word = random.choice(d[first])
    sentence.append(next_word)

    ends = ['.', '?', '!', r'"']

    # if the key/value contains a `.` or `" "`, it is a stop word -> end the sentence
    while not any(end in next_word for end in ends):
        # continue the chain to form sentences
        next_word = random.choice(d[next_word])
        sentence.append(next_word)
    
    return " ".join(sentence)

# TODO: construct 5 random sentences
print("\n----SENTENCES----\n")
print("1.", markov(words))
print("2.", markov(words))
print("3.", markov(words))
print("4.", markov(words))
print("5.", markov(words))

# paragraph form
print("\n----PARAGRAPH----\n")
print(markov(words), end=" ")
print(markov(words), end=" ")
print(markov(words), end=" ")
print(markov(words), end=" ")
print(markov(words))
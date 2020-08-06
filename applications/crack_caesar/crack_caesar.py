import string

# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

decoded = ['W', 'J', 'M', 'X', 'C', 'D', 'K', 'I', 'N', 'U', 'S', 'O', 'G', 'Q', 'B', 'Y', 'E', 'F', 'A', 'Z', 'P', 'H', 'V', 'L', 'T', 'R']

def cipher(t):
    with open(t) as f:
        text = f.read()
    
    # initialize the dictionary
    d = {}

    # split the text into words
    text = text.split()

    # iterate through the words in the `text` list
    for word in text:
        # count the occurrence of each letter for each word
        for l in word:
            # if the letter is not in the dictionary, add it
            if l not in d:
                d[l] = 0
            # increment the occurrences by + 1
            d[l] += 1

    # clean up keys in the dictionary to only include letters
    for p in string.punctuation:
        if p in d.keys():
            del d[p]
        elif '—' in d.keys():
            del d['—']
        elif "1" in d.keys():
            del d["1"]

    # sort the dictionary by letters with most occurrences
    d = sorted(sorted(d), key=d.get, reverse=True)

    # create a dictionary to map `d with `letters`
    decoded = {}

    for i in d:
        if i not in decoded:
            decoded[i] = letters.pop(0)

    # create an empty string to store the decoded text file
    answer = ""

    # for each word in the text file, iterate over the letters
    for word in text:
        # turn each word into a list for manipulating the values
        word = list(word)

        # for each letter in a word, decode it based on the decoded dictionary
        for i, l in enumerate(word):
            if l in decoded.keys():
                word[i] = decoded[l]

        # rejoin the letters into words
        word = "".join(word)

        answer = answer + " " + word

    print(answer)

cipher("ciphertext.txt")
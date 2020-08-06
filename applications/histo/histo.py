import string

# Print a histogram showing the occurrence of each word in a string
def histogram(file):
    with open(file) as f:
        strings = f.read()

    # ignore special characters, if none -> print nothing
    for p in string.punctuation:
        strings = strings.replace(p, "")

    d = {}
    # split string by spaces between words
    words = strings.split()

    for w in words:
        # ignore all cases and output lowercase
        w = w.lower()

        # log how many times the word occurs
        if w not in d:
            d[w] = 0
        d[w] += 1

    # sort by number of occurrences, and then by alphabetical order
    for w in sorted(sorted(d), key=d.get, reverse=True):
        d[w] *= "#"
        print(w.ljust(15, ' '), d[w])

histogram("robin.txt")
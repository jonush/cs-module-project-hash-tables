import string

def word_count(s):
    d = {}

    for p in string.punctuation:
        # skip apostrophes 
        if p == "'":
            continue
        # ignore punctuation and symbols
        else:
            s = s.replace(p, "")
    
    # split string into words and count occurrence of each word
    for w in s.split():
        # ignore letter case
        # output should be in lowercase
        w = w.lower()

        # count how many times each word shows up in the string
        if w not in d:
            d[w] = 0
        d[w] += 1
    
    return d

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
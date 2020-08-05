def no_dups(s):
    # input: a string of words with spaces (only a-z characters)
    # output: string with no duplicates
    # solution must be O(n)
    d = {}

    for w in s.split():
        d[w] = None

    return ' '.join(d.keys())

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
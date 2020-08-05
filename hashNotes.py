"""
Hash Tables
--------------------------------------------
"""
HASH_DATA_SIZE = 8     # O(1) over the HASH_DATA_SIZE
hash_data = [None] * HASH_DATA_SIZE

def hash_function(s):
    """this function does not account for collisions"""
    bytes_list = s.encode()

    total = 0

    """loops over the bytes in the key, NOT over the length of the hash_data"""
    for b in bytes_list: # O(n) over the length of the key
        total += b
    
    return total

def get_index(s):
    hash_value = hash_function(s)
    return hash_value % HASH_DATA_SIZE

def put(k, v):
    """for a given key, store a value in the hash table"""
    index = get_index(k)
    hash_data[index] = v

def get(k):
    """for a given key, return its value from the hash table"""
    index = get_index(k)
    return hash_data[index]

"""
Collision Resolution By Chaining
--------------------------------------------
- Make the array of slots into an array of linked lists
- Each linked list is a `HashTableEntry`

-------------- PUT --------------------
Slot Index    Chain (linked list)
----------    -------------------------
0             -> None
1             {foo: 12} -> None
2             {baz: 99} -> {bar: 30} -> None
3             -> None

put("foo", 12)  -> hashes to 1
put("bar", 30)  -> hashes to 2
put("baz", 99)  -> hashes to 2 -> collision
put("bar", 50)  -> hashes to 2 -> collision

1. Figure out the index
2. Search the linked list to see if the key is there
    2a. if the key is there, overwrite the value
    2b. If not, create a new `HashTableEntry`, and insert it in the list 

-------------- GET --------------------
Slot Index    Chain (linked list)
----------    -------------------------
0             -> None  
1             -> None 
2             -> None 
3             -> None 

1. Figure out the index for the key
2. Search the linked list at the index for the `HashTableEntry` that matches the key
    2a. If the key is there, return the value for the entry
    2b. If not, return None

-------------- DELETE --------------------
Slot Index    Chain (linked list)
----------    -------------------------
0             -> None  
1             -> None 
2             -> None 
3             -> None 

1. Figure out the index for the key
2. Search the linked list at the index for the `HashTableEntry` that matches the key
    2a. If the key is there, delete the entry from the linked list and return the value
    2b. If not, return None
"""

"""
Collision Handling with Linked Lists
-----------------------------------------------
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, value):
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return cur
            
            cur = cur.next
        return None

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node
        
    def delete(self, value):
        # special case of deleting the head of the list
        if self.head.value == value:
            old_head = self.head
            self.head = self.head.next

            return old_head
        
        # general case of deleting from the list
        prev = self.head
        cur = self.head.next

        while cur is not None:
            if cur.value == value:
                # cut the node out
                prev.next = cur.next
                return cur
            
            prev = prev.next
            cur = cur.next

        # if we get here, we didn't find the value
        return None

"""
Resizing & Load Factors
----------------------------------------------
when you PUT:
    if the load factor > 0.7:
        double the size of the array capacity
        for each element in the old array:
            PUT in the new array
"""

"""
PRACTICE PROBLEM
-----------------------------------------------
Add up and print the sum of the all of the minimum elements of each inner array:
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code.
Run through the UPER problem solving framework while going through your thought process.
"""

def add_min(nums):
    total = 0

    for i in nums:
        total += min(i)

    return total

test = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175
# print(add_min(test))

test_stretch = [
  [8, [4]], 
  [[90, 91], -1, 3], 
  [9, 62], 
  [[-7, -1, [-56, [-6]]]], 
  [201], 
  [[76, 0], 18],
]
# The expected output for the above input is:
# 8 + 4 + 90 + -1 + 9 + -7 + -56 + -6 + 201 + 0 + 18 = 260
#print(add_min(test_stretch))

"""
Fibonacci Sequence (Recursive)
----------------------------------------------
"""
cache = {} # store values in the cache

def fib(n):
    if n <= 1:
        return n

    if n not in cache: # avoid having to recompute values each time
        cache[n] = fib(n-1) + fib(n-2)

    return cache[n]

# print(f"{fib(99)}")

"""
Sorting Elements
----------------------------------------------
"""
d = {
    "foo": 12,
    "bar": 17,
    "qux": 2
}
# sort by keys
items = list(d.items())
items.sort()

# sort by values
def fun1(e):
    return e[1]

items.sort(key=fun1)

# same as:
# items.sort(key=lambda e: e[1])

# print(items)

"""
Histogram
---------------------------------------------
"""
def letter_count(s):
    d = {}

    for c in s:
        if c.isspace():
            continue

        c = c.lower()

        if c not in d:
            d[c] = 0
        d[c] += 1

    return d

# print(letter_count("Hello"))

def print_sorted_letter_count(s):
    d = letter_count(s)

    items = list(d.items())

    items.sort(key=lambda e: e[1], reverse=True)

    for i in items:
        print(f"{i[0]}: {i[1]}")

    return items

# print_sorted_letter_count("hello")

"""
Caesar Cipher
----------------------------------
"""
encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

decode_table = {}

def encode(s):
    r = ""

    for c in s:
        r += encode_table[c]

    return r

for k, v in encode_table.items():
    decode_table[v] = k

def decode(s):
    r= ""

    for c in s:
        r += decode_table[c]
    
    return r

print(encode("GOATS"))
print(decode("JEHFN"))
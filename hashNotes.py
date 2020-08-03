HASH_DATA_SIZE = 8     # O(1) over the HASH_DATA_SIZE
hash_data = [None] * HASH_DATA_SIZE

def hash_function(s):
    """this function does not account for collisions"""x
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
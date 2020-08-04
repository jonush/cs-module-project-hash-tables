class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets that accepts string keys
    Implement this.
    """

    def __init__(self, capacity = MIN_CAPACITY):
        self.data = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to head the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        return self.size / self.capacity

    def fnv1(self, key, seed = 0):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """

        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037

        hash = offset_basis + seed

        for char in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(char)

        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        hash = 5381

        for char in key:
            hash = (hash * 33) + ord(char)

        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        index = self.hash_index(key)            # find index of new node
        node = self.data[index]                 # either an existing node or None
        item = HashTableEntry(key, value)       # create a new hash table entry
        self.size += 1                          # increase size by 1 for load factor

        # if there is no node at given index:
        if node is None:
            # create and set the new node to the index  
            self.data[index] = item
        # while there is a node at the given index:
        else:
            # traverse linked list and check for existing node
            while node.next is not None and node.key != item.key:
                node = node.next
            # if the key (node) already exists, update it:
            if node.key == item.key:
                node.value = item.value
                return
            # else, set item.next to node & set the item as the node
            else:
                item.next = self.data[index]
                self.data[index] = item
        
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)

        # if self.get_load_factor() < 0.2:
        #     if self.capacity / 2 < MIN_CAPACITY:
        #         self.resize(MIN_CAPACITY)
        #     else:
        #         self.resize(self.capacity // 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        node = self.data[index]

        # if the node is the head and key matches given key, delete the node
        if node.key == key:
            old_node = node
            # set index to node.next
            self.data[index] = node.next
            # decrement size for load factor
            self.size -= 1
            return old_node.value
        
        # for general removal of nodes
        prev = node
        cur = node.next

        while cur is not None:
            if cur.key == key:
                # connect previous node to node.next
                prev.next = cur.next
                # decrement size for load factor
                self.size -= 1
                return cur.value

            prev = prev.next
            cur = cur.next

        # if the given key is not found, return None
        return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        node = self.data[index]

        # look for the desired node in the linked list
        while node is not None and node.key != key:
            node = node.next
        
        # if no node exists with the given key, return None
        if node is None:
            return None
        # else, return the node's value
        else:
            return node.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # resize the hash table to the new capacity
        self.capacity = new_capacity
        # store instance of old hash table values
        old_data = self.data
        # create new hash table with new capacity
        self.data = [None] * new_capacity
        # rehash elements and integrate into new hash table
        for i in range(len(old_data)):
            old_hash = old_data[i]

            # if the hash item exists
            if old_hash:
                # traverse linked list if it exists
                while old_hash is not None:
                    self.put(old_hash.key, old_hash.value)
                    old_hash = old_hash.next

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    head_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    itemcity = ht.get_num_slots()

    print(f"\nResized from {head_capacity} to {itemcity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")

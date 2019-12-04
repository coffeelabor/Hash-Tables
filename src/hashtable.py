# '''
# Linked List hash table key/value pair
# '''

class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

        #Might need to add self.count to track table load and resize as needed

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # I need to put the key at an index in the array
        #I need to check if the hashTable is full.  Maybe use that double_size from lecture
        # If the index is > than the count (might need to add count) then Error out of rang
        # Somehow use the key as the index of where to insert the value (hashed key I think)
        # print(f"key_index {key_index}")
        
        # if self.storage[key_index] is not None:
        #     print(f"O no: Overwriting data at {key_index}")
            # self.resize()
        # self.storage[key_index] = value
        # self.storage[key_index] = LinkedPair(key, value)
        key_index = self._hash_mod(key)

        current_pair = self.storage[key_index]
        last_pair = None

        while current_pair is not None and current_pair.key != key:
            last_pair = current_pair
            current_pair = last_pair.next

        if current_pair is not None:
            current_pair.value = value
        else:
            new_pair = LinkedPair(key, value)
            new_pair.next = self.storage[key_index]
            self.storage[key_index] = new_pair

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        key_index = self._hash_mod(key)
        if self.storage[key_index] is None:
            # print(f'warning if the key is not found')
            return
        self.storage[key_index] = None


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        key_index = self._hash_mod(key)

        current_pair = self.storage[key_index]

        while current_pair is not None:
            if(current_pair.key == key):
                return current_pair.value
            current_pair = current_pair.next

        # if self.storage[key_index] is not None:
        #     if self.storage[key_index].key == key:
        #         return self.storage[key_index].value
        #     else:
        #         # print(f'Bruh what are you doing: Key doesnt match')
        #         return None
        # else:
        #     return None
    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # self.capacity *= 2
        # new_storage = [None] * self.capacity

        # # for i in range(self.count):
        # #     new_storage[i] = self.storage[i]
        # for bucket_item in self.storage:
        #     # new_storage[]
        #     if bucket_item is not None:
        #         new_index = self._hash_mod(bucket_item.key)
        #         new_storage[new_index] = LinkedPair(bucket_item.key, bucket_item.value)

        # self.storage = new_storage

        old_storage = self.storage
        self.capacity = 2 * self.capacity
        self.storage = [None] * self.capacity
        current_pair = None
        for bucket_item in old_storage:
            current_pair = bucket_item
            while current_pair is not None:
                self.insert(current_pair.key, current_pair.value)
                current_pair = current_pair.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

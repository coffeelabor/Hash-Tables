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

        key_index = self._hash_mod(key)
        print('key_index in insert', key_index)
        current_pair = self.storage[key_index]
        print('current_pair in insert', current_pair)
        last_pair = None
        print('last_pair in inser', last_pair)

        while current_pair != None and current_pair.key != key:
            print('current_pair in insert/while', current_pair)
            last_pair = current_pair
            print('last_pair in insert/while', last_pair)
            current_pair = last_pair.next
            print('current_pair in insert/while.next', current_pair)
        
        if current_pair != None:
            current_pair.value = value
            print('current_pair in insert/if', current_pair.value)
        
        else:
            temp = LinkedPair(key, value)
            print('temp in inser/else', temp)
            temp.next = self.storage[key_index]
            self.storage[key_index] = temp
            print('self.storage in inser/else', self.storage[key_index])



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        pass


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        key_index = self._hash_mod(key)

        current_pair = self.storage[key_index]

        while current_pair != None:
            if(current_pair.key == key):
                return current_pair.value
            current_pair = current_pair.next


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity = 2 * self.capacity
        self.storage = [None] * self.capacity
        current_pair = None
        for old_item in old_storage:
            current_pair = old_item
            while current_pair != None:
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



# ##################################################
'''
 def insert(self, key, value):
        
    # Store the value with the given key.

    # Hash collisions should be handled with Linked List Chaining.

    # Fill this in.
    
    index = self._hash_mod(key)

    if self.storage[index] != None:
        print(f"Warning: collsion has occured at {index}")

        return
    
    else: 
        self.storage[index] = (key, value)
        return
    
    return

# check this again, might of missed something
def remove(self, key):

    index = self._hash_mod(key)
    if self.storage[index] != None:
        if self.storage[index][0] == key:
            self.storage[index] = None
        else:
            print(f"Waring: Collision has occured at {index})

        return
    
    else: 
        print(f"Waring key({key}) not found)
    
    return

# check this again, might of missed something
def retrieve(self, key):
    index = self._hash_mod(key)
    if self.storage[index] != None:
        if self.storage[index][0] == key:
            reutrn self.storage[index][1] = None
        else:
            print(f"Waring: Collision has occured at {index})

        return
    
    else: 
        return none
    
    return

def resize(self):
      
    old_storage = self.storage
    self.capacity = 2 * self.capacity
    self.storage = [None] * self.capacity
    current_pair = None
    for old_item in old_storage:
        self.insert(item[0], item[1])
'''

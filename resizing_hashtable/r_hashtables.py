# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for char in string:
        hash = ((hash << 5) + hash) + ord(char)

    return (hash % max)


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)

    pair_stored = hash_table.storage[index]

    pair_to_insert = LinkedPair(key, value)

    if hash_table.storage[index] is None:
        # insert new pair
        hash_table.storage[index] = pair_to_insert
    else:
        if pair_stored.key == key:
            hash_table.storage[index].value = value
            return None
        while pair_stored.next is not None:
            # move to the next
            pair_stored = pair_stored.next
            if pair_stored.key == key:
                pair_stored.value = value
                return None
        if pair_stored.next is None:
            pair_stored.next = pair_to_insert

    print(hash_table.storage)

    # '''
    # Fill this in.

    # If you try to remove a value that isn't there, print a warning.
    # '''


def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    pair_stored = hash_table.storage[index]
    pair_last = None

    while pair_stored is not None and pair_stored.key != key:
        pair_last = pair_stored
        pair_stored = pair_last.next
    if pair_stored is None:
        print("Warning, you tring to remove a value that isn't there")
    else:
        if pair_last is None:
            hash_table.storage[index] = pair_stored.next
        else:
            pair_last.next = pair_stored.next


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)

    while hash_table.storage[index] is not None:
        print("1", hash_table.storage[index].key, key)
        if hash_table.storage[index].key == key:
            print("2", hash_table.storage[index].key, key)
            return hash_table.storage[index].value
        print("3", hash_table.storage[index].next)
        hash_table.storage[index] = hash_table.storage[index].next


def hash_table_resize(hash_table):
    new_table = HashTable(2 * hash_table.capacity)
    current_pair = None

    for i in range(hash_table.capacity):
        current_pair = hash_table.storage[i]
        while current_pair is not None:
            hash_table_insert(
                new_table, current_pair.key, current_pair.value)
            current_pair = current_pair.next
    hash_table = new_table
    return hash_table


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()

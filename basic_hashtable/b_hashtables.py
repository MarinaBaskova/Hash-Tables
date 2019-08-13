

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for char in string:
        hash = ((hash << 5) + hash) + ord(char)
        print(hash)
    return (hash % max)

# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# print(f"warning, you will be overwriting {hash_table.storage[index].key}")
# '''


def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    pair_insert = Pair(key, value)
    pair_stored = hash_table.storage[index]

    if pair_stored is not None:
        if pair_insert.key != pair_stored.key:
            print("warning, it will overwrite old key value pair")
    hash_table.storage[index] = pair_insert


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''


def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is None or hash_table.storage[index].key != key:
        print("warning, unable to remove item with provided key")
    hash_table.storage[index] = None

# '''
# Fill this in.

# Should return None if the key is not found.
# '''


def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is not None:
        if hash_table.storage[index].key == key:
            return hash_table.storage[index].value
    print("can not find the value with the provided key")
    return None


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()

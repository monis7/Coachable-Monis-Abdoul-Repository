class Node:
    """ Node for separate chaining in case of collisions """
    def __init__(self, key: str, value: int):
        self.key = key
        self.value = value
        self.next = None  # Points to next node in case of collisions

class HashMapChaining:
    """ Fixed-size HashMap using separate chaining for collision handling """
    
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.size = 0
        self.buckets = [None] * max_size  # Array of linked list heads
        self.min_key = None
        self.max_key = None

    def _hash_function(self, key: str) -> int:
        """ Custom hash function based on sum of ASCII values of characters """
        return sum(ord(c) for c in key) % self.max_size

    def put(self, key: str, value: int):
        """ Inserts a key-value pair into the HashMap """
        if self.size >= self.max_size:
            print("Error: HashMap is full.")
            return

        index = self._hash_function(key)
        node = self.buckets[index]

        if node is None:
            self.buckets[index] = Node(key, value)
        else:
            # Collision: Separate chaining (linked list)
            prev = None
            while node:
                if node.key == key:
                    node.value = value  # Update value if key exists
                    return
                prev, node = node, node.next
            prev.next = Node(key, value)  # Append at the end

        self.size += 1
        self._update_min_max_keys(key)

    def get(self, key: str) -> int:
        """ Retrieves a value by key, returns None if not found """
        index = self._hash_function(key)
        node = self.buckets[index]

        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None  # Key not found

    def _update_min_max_keys(self, key: str):
        """ Efficiently updates min and max keys """
        if self.min_key is None or key < self.min_key:
            self.min_key = key
        if self.max_key is None or key > self.max_key:
            self.max_key = key

    def get_min_key(self) -> str:
        """ Returns the smallest key in the HashMap """
        return self.min_key

    def get_max_key(self) -> str:
        """ Returns the largest key in the HashMap """
        return self.max_key

class HashMapProbing:
    """ Fixed-size HashMap using open addressing (linear probing) """

    def __init__(self, max_size: int):
        self.max_size = max_size
        self.size = 0
        self.buckets = [None] * max_size  # Array for key-value storage
        self.min_key = None
        self.max_key = None

    def _hash_function(self, key: str) -> int:
        """ Custom hash function """
        return sum(ord(c) for c in key) % self.max_size

    def put(self, key: str, value: int):
        """ Inserts a key-value pair into the HashMap using linear probing """
        if self.size >= self.max_size:
            print("Error: HashMap is full.")
            return

        index = self._hash_function(key)
        original_index = index

        while self.buckets[index] is not None:
            stored_key, _ = self.buckets[index]
            if stored_key == key:
                self.buckets[index] = (key, value)  # Update existing key
                return
            index = (index + 1) % self.max_size  # Linear probing

            if index == original_index:
                print("Error: No available slot found.")
                return

        self.buckets[index] = (key, value)
        self.size += 1
        self._update_min_max_keys(key)

    def get(self, key: str) -> int:
        """ Retrieves a value by key using linear probing """
        index = self._hash_function(key)
        original_index = index

        while self.buckets[index] is not None:
            stored_key, value = self.buckets[index]
            if stored_key == key:
                return value
            index = (index + 1) % self.max_size  # Continue probing

            if index == original_index:
                return None  # Not found

        return None

    def remove(self, key: str):
        """ Removes a key-value pair from the HashMap using lazy deletion """
        index = self._hash_function(key)
        original_index = index

        while self.buckets[index] is not None:
            stored_key, _ = self.buckets[index]
            if stored_key == key:
                self.buckets[index] = None  # Mark as deleted
                self.size -= 1
                return
            index = (index + 1) % self.max_size

            if index == original_index:
                return  # Key not found

    def _update_min_max_keys(self, key: str):
        """ Efficiently updates min and max keys """
        if self.min_key is None or key < self.min_key:
            self.min_key = key
        if self.max_key is None or key > self.max_key:
            self.max_key = key

    def get_min_key(self) -> str:
        """ Returns the smallest key in the HashMap """
        return self.min_key

    def get_max_key(self) -> str:
        """ Returns the largest key in the HashMap """
        return self.max_key

import unittest

class TestHashMap(unittest.TestCase):

    def test_chaining_hashmap(self):
        hashmap = HashMapChaining(10)
        hashmap.put("apple", 10)
        hashmap.put("banana", 20)
        hashmap.put("cherry", 30)

        self.assertEqual(hashmap.get("apple"), 10)
        self.assertEqual(hashmap.get("banana"), 20)
        self.assertEqual(hashmap.get("cherry"), 30)
        self.assertEqual(hashmap.get("pear"), None)

        self.assertEqual(hashmap.get_min_key(), "apple")
        self.assertEqual(hashmap.get_max_key(), "cherry")

    def test_probing_hashmap(self):
        hashmap = HashMapProbing(10)
        hashmap.put("apple", 10)
        hashmap.put("banana", 20)
        hashmap.put("cherry", 30)

        self.assertEqual(hashmap.get("apple"), 10)
        self.assertEqual(hashmap.get("banana"), 20)
        self.assertEqual(hashmap.get("cherry"), 30)

        hashmap.remove("banana")
        self.assertEqual(hashmap.get("banana"), None)

        self.assertEqual(hashmap.get_min_key(), "apple")
        self.assertEqual(hashmap.get_max_key(), "cherry")

if __name__ == '__main__':
    unittest.main()


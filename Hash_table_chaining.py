# Part 2: Hash Table with Chaining Implementation
class HashTableChaining:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0

    def hash_function(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        idx = self.hash_function(key)
        for pair in self.table[idx]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[idx].append([key, value])
        self.size += 1
        if self.size / self.capacity > 0.7:
            self._resize()

    def search(self, key):
        idx = self.hash_function(key)
        for pair in self.table[idx]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        idx = self.hash_function(key)
        for i, pair in enumerate(self.table[idx]):
            if pair[0] == key:
                del self.table[idx][i]
                self.size -= 1
                return True
        return False

    def _resize(self):
        new_capacity = self.capacity * 2
        new_table = [[] for _ in range(new_capacity)]
        for bucket in self.table:
            for key, value in bucket:
                idx = hash(key) % new_capacity
                new_table[idx].append([key, value])
        self.capacity = new_capacity
        self.table = new_table

# Testing the hash table
hash_table = HashTableChaining()
for i in range(15):
    hash_table.insert(f"key{i}", i)

for i in range(15):
    print(f"Search key{i}: {hash_table.search(f'key{i}')}")

for i in range(5):
    hash_table.delete(f"key{i}")
    print(f"Deleted key{i}")

print("Final Hash Table:", hash_table.table)
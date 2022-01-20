class Bucket:
    def __init__(self):
        self.bucket = []
        
    def update(self, key, value):
        is_find = False
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                self.bucket[i] = (key, value)
                is_find = True
                break
        
        if not is_find:
            self.bucket.append((key, value))
    
    def get(self, key):
        for k, v in self.bucket:
            if k == key:
                return v
        
        return -1
    
    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                del self.bucket[i]
        
    
class MyHashMap:

    def __init__(self):
        self.size = 100
        self.hash_map = [Bucket()] * self.size

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.size
        self.hash_map[hash_key].update(key, value)

    def get(self, key: int) -> int:
        hash_key = key % self.size
        return self.hash_map[hash_key].get(key)

    def remove(self, key: int) -> None:
        hash_key = key % self.size
        self.hash_map[hash_key].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
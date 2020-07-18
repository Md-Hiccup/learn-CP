class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_bucket = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.hash_bucket[key] = value           

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        del self.hash_bucket[key]
            

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.hash_bucket:
            return self.hash_bucket[key]
        return -1


# Your MyHashSet object will be instantiated and called as such:
hashMap = MyHashMap()
hashMap.put(1, 1)   
hashMap.put(2, 2)         
get = hashMap.get(1)          # returns 1
print(get)
get = hashMap.get(3)          # returns -1 (not found)
print(get)
hashMap.put(2, 1)         # update the existing value
get = hashMap.get(2)          # returns 1 
print(get)
hashMap.remove(2)       # remove the mapping for 2
get = hashMap.get(2)
print(get)
print(hashMap.hash_bucket)
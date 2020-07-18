class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_bucket = set()

    def add(self, key: int) -> None:
        self.hash_bucket.add(key)
            

    def remove(self, key: int) -> None:
        self.hash_bucket.discard(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.hash_bucket:
            return True
        return False
        
    def main(self) -> None:
        self.add(1)
        self.add(2)
        print('Values in hashset:', self.hash_bucket)
        get = self.contains(1)     # returns true
        print('1 is in hashset:', get)
        get = self.contains(3)     # returns false (not found)
        print('3 is in hashset:', get)
        self.add(2)          
        get = self.contains(2)     # returns true
        print('2 is in hashset:', get)
        print('Remove 2 from hashset')
        self.remove(2)
        get = self.contains(2)
        print('2 is in hashset:', get)


def hashset_1():
    # 1. initialize the hash set
    hashset = set() 
    # 2. add a new key
    hashset.add(3)
    hashset.add(2)
    hashset.add(1)
    print("Value in hash set:", hashset)
    # 3. remove a key
    print("Remove 2 from hash set")
    hashset.remove(2)
    # 4. check if the key is in the hash set
    if (2 not in hashset):
        print("Key 2 is not in the hash set.")
    # 5. get the size of the hash set
    print("Size of hashset is:", len(hashset)) 
    # 6. iterate the hash set
    for x in hashset:
        print(x, end=" ")
    print("are in the hash set.")
    # 7. clear the hash set
    print("Clear the hash set")
    hashset.clear()                         
    print("Size of hashset:", len(hashset))



if __name__ == "__main__":
    
    #### 1. Simple Intro
    # Your MyHashSet object will be instantiated and called as such:
    # hashSet = MyHashSet()
    # hashSet.main()

    #### 2. Hash Set Code
    hashset_1()

    


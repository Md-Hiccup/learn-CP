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


def containsDuplicate(arr):
    """
    Given an array of integers, find if the array contains any duplicates.
    Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
    Example:
        Input: [1,2,3,1]
        Output: true
    """
    print(f'Arr: {arr}')

    ### 1 - Hash Table
    # hash_bucket = set(arr)
    # if len(hash_bucket) != len(arr):
    #     return True
    # return False

    ### 2 - Hash Table
    hash_set = set()
    for i in arr:
        if i in hash_set:
            return True
        hash_set.add(i)
    return False


def singleNumber(arr):
    """
    Given a non-empty array of integers, every element appears twice except for one. Find that single one.
    Example:
        Input: [2,2,1]
        Output: 1
    """
    print(f'Arr: {arr}')

    ### 1 - Hash Set
    # ls = set(arr)
    # for i in ls:
    #     if nums.count(i) == 1:
    #         return i

    ### 1.1 - Hash Set
    # from collections import defaultdict
    # hashtable = defaultdict(int)
    # for i in arr:
    #     hashtable[i] += 1

    # for i in hashtable:
    #     if hashtable[i] == 1:
    #         return i

    ### 2 - XOR
    a = 0
    for i in arr:
        a ^= i
    return a


def intersection(arr1, arr2):
    """
    Given two arrays, write a function to compute their intersection.
    Example 1:
        Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        Output: [9,4]
    """
    print(f'Arr1: {arr1}\nArr2: {arr2}')
    hashset1 = set(arr1)
    hashset2 = set(arr2)

    # 1 - Built-in (intersection or &)
    res = list(hashset1 & hashset2)

    # 2 - hash table with search
    # if len(hashset1) < len(hashset2):
    #     res = [x for x in hashset1 if x in hashset2]
    # else:
    #     res = [x for x in hashset2 if x in hashset1]

    # 3 - Set Difference
    # res = list(hashset2 - (hashset2 - hashset1))

    return res


def isHappy(n):
    """
    Write an algorithm to determine if a number n is "happy".

    A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

    Return True if n is a happy number, and False if not.

    Example:
        Input: 19
        Output: true
        Explanation:
            1^2 + 9^2 = 82
            8^2 + 2^2 = 68
            6^2 + 8^2 = 100
            1^2 + 0^2 + 0^2 = 1
    """
    print("Number: ", n)
    hashset = set()

    while( n!= 1):
        temp = n
        tot = 0

        while(temp != 0):
            rem = temp % 10
            tot += rem ** 2
            temp = temp // 10

        if tot in hashset:
            return False

        hashset.add(tot)
        n = tot

    return True



if __name__ == "__main__":

    # #### 1. Simple Intro to Hash Set
    # # Your MyHashSet object will be instantiated and called as such:
    hashSet = MyHashSet()
    hashSet.main()

    print('*'*40)

    # #### 2. Hash Set Example Code
    hashset_1()

    print('*'*40)

    # #### 3. Contains Duplicate
    print("To Check Hashset containing Duplicate value or not")
    # # print("Enter the value with space separated to insert in hashset")
    # # arr = list(map(int, input().strip().split()))

    arr = [1, 1, 2, 3, 4, 5, 4]
    is_duplicate = containsDuplicate(arr)
    print('Is duplicate: ', is_duplicate)

    print('*'*40)

    # #### 4. Single Number
    # # print("Enter the value with space separated")
    # # arr = list(map(int, input().strip().split()))

    arr = [1, 1, 2, 2, 3, 3, 4]
    single = singleNumber(arr)
    print('Single No:', single)

    print('*'*40)

    # #### 5. Intersection of Two Arrays
    # # print("Enter value in Array 1 with space separated")
    # # arr1 = list(map(int, input().strip().split()))
    # # print("Enter value in Array 2 with space separated")
    # # arr2 = list(map(int, input().strip().split()))

    arr1 = [4, 9, 5, 3]
    arr2 = [9, 4, 9, 8, 4]
    intrsct = intersection(arr1, arr2)
    print("Intersection of Two Arrays:", intrsct)

    print('*'*40)

    # #### 6. Happy Number
    # # print('Enter the Number to check, it is Happy')
    # # numb = int(input())
    numb = 210 #19

    is_happy = isHappy(numb)
    print("Is Number Happy:", is_happy)

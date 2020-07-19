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

    def main(self):
        self.put(1, 1)
        self.put(2, 2)
        print('Values in hash map:', self.hash_bucket)
        get = self.get(1)          # returns 1
        print('Is 1 in hash map:', get)
        get = self.get(3)          # returns -1 (not found)
        print('Is 3 in hash map:', get)
        self.put(2, 1)         # update the existing value
        get = self.get(2)          # returns 1
        print('Is 2 in hash map:', get)
        print('Remove 2 from hash map')
        self.remove(2)       # remove the mapping for 2
        get = self.get(2)
        print('Is 2 in hash map:', get)
        print(self.hash_bucket)


def hashmap_1():
    # 1. initialize a hash map
    hashmap = {0 : 0, 2 : 3}
    # 2. insert a new (key, value) pair or update the value of existed key
    hashmap[1] = 1
    hashmap[1] = 2
    print("Value in hash map", hashmap)
    # 3. get the value of a key
    print("The value of key 1 is: " + str(hashmap[1]))
    # 4. delete a key
    print("Remove 2 from hash map")
    del hashmap[2]
    # 5. check if a key is in the hash map
    if 2 not in hashmap:
        print("Key 2 is not in the hash map.")
    # 6. both key and value can have different type in a hash map
    hashmap["pi"] = 3.1415
    # 7. get the size of the hash map
    print("The size of hash map is: " + str(len(hashmap)))
    # 8. iterate the hash map
    for key in hashmap:
        print("(" + str(key) + "," + str(hashmap[key]) + ")", end=" ")
    print("are in the hash map.")
    # 9. get all keys in hash map
    print("All keys in hash map")
    print(hashmap.keys())
    # 10. clear the hash map
    print("Clear the hash map")
    hashmap.clear()
    print("The size of hash map is: " + str(len(hashmap)))


def twoSum(arr, t):
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    Example:
        nums = [2, 7, 11, 15], target = 9,

        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
    """
    print(f"Arr: {arr}\ntarget: {t}")

    ### 1 - Brute Force O(n^2)
    # for i in range(len(nums)):
    #     if target - nums[i] in nums[i+1:]:
    #         d  = [i, nums[i+1:].index(target-nums[i]) + i+1]
    #         print(d)
    #         return d

    ### 2 - Two pass Hash Table
    # hashmap = {}
    # for i in range(len(arr)):
    #     hashmap[arr[i]] = i

    # for i in range(len(arr)):
    #     comp = t-arr[i]
    #     # # Check Key exist in hashmap
    #     # # Check value of key index != i
    #     if comp in hashmap and hashmap[comp] != i:
    #         return [i, hashmap[comp]]

    ### 3 - One pass Hash Table
    hashmap = {}
    for i in range(len(arr)):
        comp = t - arr[i]
        if comp in hashmap:
            return [i, hashmap[comp]]
        hashmap[arr[i]] = i


def isIsomorphic(s, t):
    """
    Given two strings s and t, determine if they are isomorphic.

    Two strings are isomorphic if the characters in s can be replaced to get t.

    All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

    Example 1:
        Input: s = "egg", t = "add"
        Output: true

        Input: s = "paper", t = "title"
        Output: true

        Input: s = "foo", t = "bar"
        Output: false
    """
    print(f"String 1: {s}\nString 2: {t}")

    if len(s) != len(t):
        return False

    hashmap = {}
    hashset = set()
    for i in range(len(s)):
        c1 = s[i]
        c2 = t[i]
        if c1 in hashmap:
            if hashmap[c1] != c2:
                return False
        else:
            if c2 in hashset:
                return False
        hashmap[c1] = c2
        hashset.add(c2)
        # print(hashmap, hashset)
    return True


def findRestaurant(arr1, arr2):
    """
    Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

    You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

    Example 1:
        Input:  ["Shogun", "Tapioca Express", "Burger King", "KFC"]
                ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
        Output: ["Shogun"]
        Explanation: The only restaurant they both like is "Shogun".
    Example 2:
        Input:  ["Shogun", "Tapioca Express", "Burger King", "KFC"]
                ["KFC", "Shogun", "Burger King"]
        Output: ["Shogun"]
        Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
    Example 3:
        Input:  ["Shogun","Tapioca Express","Burger King","KFC"]
                ["KFC","Burger King","Tapioca Express","Shogun"]
        Output: ["KFC","Burger King","Tapioca Express","Shogun"]
        Explaination: All the restaurant they both like so return all the restaurant.
    """
    # arr1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    # arr2 = ["KFC","Burger King","Tapioca Express","Shogun"]
    print(f"Array1: {arr1}\nArray2: {arr2}")

    ### 1. - With 2 Hash Map
    # hashmap = {}
    # for i in range(len(arr1)):
    #     hashmap[arr1[i]] = i

    # hashmap2 = {}
    # for j in range(len(arr2)):
    #     if arr2[j] in hashmap:
    #         ind = hashmap[arr2[j]] + j
    #         if ind in hashmap2:
    #             hashmap2[ind].append(arr2[j])
    #         else:
    #             hashmap2[ind] = [arr2[j]]
    # mini = min(list(hashmap2.keys()))
    # re8turn hashmap2[mini]


    ### 2. - With 1 Hash Map
    hashmap = {}
    for i in range(len(arr1)):
        hashmap[arr1[i]] = i

    res = []
    min_sum = 100000
    sum = -1
    for j in range(len(arr2)):
        if arr2[j] in hashmap:
            sum = j + hashmap[arr2[j]]
            if sum < min_sum:
                res = []
                res.append(arr2[j])
                min_sum = sum
            elif sum == min_sum:
                res.append(arr2[j])

    return res


def firstUniqChar(s):
    """
    Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
    Examples:
        s = "leetcode"
        return 0.

        s = "loveleetcode"
        return 2.
    """
    print(f"String: {s}")
    # s = 'leetcode'
    # s = ''
    ### 1 - usin Hash Map
    hashmap = {}
    for i in range(len(s)):
        if s[i] in hashmap:
            hashmap[s[i]] += 1
        else:
            hashmap[s[i]] = 1

    for ind, ch in enumerate(s):
        if hashmap[ch] == 1:
            return ind
    return -1


def intersect(arr1, arr2):
    """
    Given two arrays, write a function to compute their intersection.

    Example 1:
        Input: nums1 = [1,2,2,1], nums2 = [2,2]
        Output: [2,2]
    Example 2:
        Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        Output: [4,9]

    Follow up:

    1. What if the given array is already sorted? How would you optimize your algorithm?
    2. What if nums1's size is small compared to nums2's size? Which algorithm is better?
    3. What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
    """
    print(f'Array1: {arr1}\nArray2: {arr2}')

    ### Follow up: - Using Hashmap
    # 2. Its already we are checking below and processing code with hashmap.
    # 3. Then need to chunks nums2 and resolve chunk with hashmap.

    hashmap = {}
    if len(arr2) < len(arr1):
        intersect(arr2, arr1)

    for i in arr1:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1

    res = []
    for i in arr2:
        if i in hashmap and hashmap[i] > 0:
            res.append(i)
            hashmap[i] -= 1

    ### Follow up. - Using Two pointer technique
    # 1. Previously assuming both arrays are sorted.
    # arr1 = sorted(arr1)
    # arr2 = sorted(arr2)
    # res = []
    # i = j = 0
    # while (i < len(arr1) and j < len(arr2)):
    #     if arr1[i] == arr2[j]:
    #         res.append(arr1[i])
    #         i += 1
    #         j += 1
    #     elif arr1[i] < arr2[j]:
    #         i += 1
    #     else:
    #         j += 1

    return res


def containsNearbyDuplicate(arr1, k):
    """
    Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

    Example 1:
        Input: nums = [1,2,3,1], k = 3
        Output: true
    Example 2:
        Input: nums = [1,0,1,1], k = 1
        Output: true
    Example 3:
        Input: nums = [1,2,3,1,2,3], k = 2
        Output: false
    """





if __name__ == "__main__":

    # #### 1. Simple Intro to Hash Map
    # # Your MyHashMap object will be instantiated and called as such:
    # hashMap = MyHashMap()
    # hashMap.main()

    # print('*'*40)

    # #### 2. Hash Map Example Code
    # hashmap_1()

    # print('*'*40)

    # #### 3. Two Sum
    # # print("Enter value in Array 1 with space separated")
    # # arr1 = list(map(int, input().strip().split()))

    # arr = [2, 7, 7, 11, 15]
    # target = 9
    # two_sum = twoSum(arr, target)
    # print("Two Sum index value:", two_sum)

    # print('*'*40)

    # #### 4. Isomorphic Strings
    # # print("Enter two strings with space separated")
    # # s, t = list(map(int, input().strip().split()))

    # s, t = ['acab', 'xcxy']
    # is_isomorphic = isIsomorphic(s, t)
    # print("Is Isomorphic Strings:", is_isomorphic)

    # print('*'*40)

    # ### 5. Minimun Index Sum of Two Lists (Favourite Restaurant)
    # # print("Enter list of restaurant in Array 1 with space separated")
    # # arr1 = list(map(int, input().strip().split()))
    # # print("Enter list of restaurant in Array 2 with space separated")
    # # arr2 = list(map(int, input().strip().split()))

    # arr1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    # arr2 = ["KFC", "Shogun", "Burger King"]
    # rest = findRestaurant(arr1, arr2)
    # print('Favourite Restaurant:', rest)

    # print('*'*40)

    # ### 5. First Unique Character in a String
    # # print("Enter a string")
    # # s = list(map(int, input().strip().split()))

    # s = 'loveleetcode'
    # res = firstUniqChar(s)
    # print('First Unique Characer is at Index:', res)

    # print('*'*40)

    # ### 5. Intersect of Two Arrays - II
    # # print("Enter list of restaurant in Array 1 with space separated")
    # # arr1 = list(map(int, input().strip().split()))
    # # print("Enter list of restaurant in Array 2 with space separated")
    # # arr2 = list(map(int, input().strip().split()))

    # arr1 = [4,9,5]
    # arr2 = [9,4,9,8,4]
    # res = intersect(arr1, arr2)
    # print('Intersection of two array:', res)

    print('*'*40)

    # ### 6. Contains Duplicate - II
    # # print("Enter numbers in Array with space separated")
    # # arr1 = list(map(int, input().strip().split()))
    # # print("Enter the difference value")
    # # k = int(input())

    arr1 = [1, 2, 3, 1]
    k = 3
    contains_duplicate = containsNearbyDuplicate
    print("Containse near by duplicate:", contains_duplicate)

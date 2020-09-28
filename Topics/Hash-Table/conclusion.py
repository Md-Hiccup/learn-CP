def numJewelsInStones(J, S):
    """
    You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

    The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

    Example 1:
        Input: J = "aA", S = "aAAbbbb"
        Output: 3
    Example 2:
        Input: J = "z", S = "ZZ"
        Output: 0
    """

    hashset = set(list(J))
    count = 0
    for i in S:
        if i in hashset:
            count += 1

    return count


def lenghtOfLongestSubstring(s):
    """
    Given a string, find the length of the longest substring without repeating characters.

    Example 1:
        Input: "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.
    Example 2:
        Input: "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.
    Example 3:
        Input: "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
                    Note that the answer must be a substring, "pwke" is a subsequence and not a substring
    """
    s = 'dvdf'
    hashset = set()
    count = 0
    tot = 0
    for i in s:
        if i in hashset:
            if tot < count:
                tot = count
            count = 0
            hashset.discard(i)
        hashset.add(i)
        count += 1
        print(hashset, count)
    if tot < len(hashset):
        return len(hashset)
    return tot


if __name__ == "__main__":

    # ### 1. Jewels and Stones
    # # print("Enter Jewels and Stones with space separated value")
    # # J, S = list(map(str, input().strip().split()))

    J = 'aA'
    S = 'aAAbbbb'
    num_jewels_in_stones = numJewelsInStones(J, S)
    print("No. of Jewels in Stones:", num_jewels_in_stones)

    print('*' * 40)

    # ### 2. Longest substring without repeating characters
    # # print("Enter the String")
    # # s = input()

    s = "abcabc"
    sub = lenghtOfLongestSubstring(s)
    print("Longest substring without repeating characters:", sub)
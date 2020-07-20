def groupAnagram(arr):
    """
    Given an array of strings, group anagrams together.
    Example:
        Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
        Output:
        [
            ["ate","eat","tea"],
            ["nat","tan"],
            ["bat"]
        ]
    """
    print(f"Array: {arr}")
    hashmap = {}
    for i in arr:
        key = ''.join(sorted(i))
        if key in hashmap:
            hashmap[key].append(i)
        else:
            hashmap[key] = [i]
    res = list(hashmap.values())
    return res


def validSudoku(mat):
    """
    Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

        1. Each row must contain the digits 1-9 without repetition.
        2. Each column must contain the digits 1-9 without repetition.
        3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    Input:
        [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
        ]
    Output: false
        Explanation: Same as Example 1, except with the 5 in the top left corner being
            modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
    """
    # print("Matrix:")
    # for i in mat:
    #     print(i)

    # To check unique value in particular Box[3x3]
    def notInBox(mat, row, col):
        st = set()
        for r in range(3):
            for c in range(3):
                curr = mat[r + row][c + col]
                if curr in st:
                    return False
                if curr != '.':
                    st.add(curr)
        return True

    # To check unique value in particular row
    def notInRow(mat, row):
        st = set()
        for i in range(9):
            if mat[row][i] in st:
                return False

            if mat[row][i] != '.':
                st.add(mat[row][i])

        return True

    # To check unique value in particular column
    def notInCol(mat, col):
        st = set()
        for j in range(9):
            if mat[j][col] in st:
                return False

            if mat[j][col] != '.':
                st.add(mat[j][col])
        return True

    # Main function to check validation in row, column and box[3x3]
    def isValid(mat, row, col):
        # return notInRow(mat, row) and notInCol(mat, col)
        # return notInCol(mat, col)
        return (notInRow(mat, row) and notInCol(mat, col) and notInBox(mat, row - row % 3, col - col % 3))

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if not isValid(mat, i, j):
                return False
    return True

    # To get Box row and col.
    # key = (i // 3) * 3 + (j // 3)



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def traverse(self, root):
        if root == None:
            return
        print(root.val, end=' ')
        self.traverse(root.left)
        self.traverse(root.right)

def findDuplicateSubtrees(root):
    """
    Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.
    Two trees are duplicate if they have the same structure with same node values.

    Example 1:
            1
            / \
            2   3
            /   / \
            4   2   4
                /
                4
        The following are two duplicate subtrees:
            2
            /
            4
        and
            4
        Therefore, you need to return above trees' root in the form of a list.
    """
    ### Link: https://leetcode.com/articles/find-duplicate-subtrees/
    ### Link: https://stackoverflow.com/questions/5900578/how-does-collections-defaultdict-work
    ### 1 - Depth First Search
    # from collections import Counter
    # count = Counter()
    # ans = []
    # def getDup(node):
    #     if node == None:
    #         return 'X'

    #     serial = '{},{},{}'.format(node.val, getDup(node.left), getDup(node.right))
    #     count[serial] += 1
    #     if count[serial] == 2:
    #         ans.append(node)
    #     return serial

    # getDup(root)
    # return ans


    ### 2 - Unique Identifier
    from collections import defaultdict, Counter
    hashmap = defaultdict()
    hashmap.default_factory = hashmap.__len__
    count = Counter()
    ans = []

    def lookup(node):
        if node:
            uid = hashmap[node.val, lookup(node.left), lookup(node.right)]
            count[uid] += 1
            # print(hashmap, count)
            if count[uid] == 2:
                ans.append(node)
            return uid


    lookup(root)
    return ans





if __name__ == "__main__":
    ### 1. Group Anagram
    # # print("Enter the array to group anagram with space separated value")
    # # arr = list(map(int, input.strip().split())

    arr = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    group_anagram = groupAnagram(arr)
    print('Group Anagram: ', group_anagram)

    print('*' * 40)

    # # print("Enter sudoku value for validate")
    # # arr[i][j] = 0
    # # for i in range(9):
    # #     for j in range(9)
    #           arr[i][j] = input().strip()

    mat = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    valid_sudoku = validSudoku(mat)
    print("Is Valid Sudoku:", valid_sudoku)

    print('*' * 40)

    # # print('Enter the Tree)
    obj = TreeNode(1)
    obj.left = TreeNode(2)
    obj.left.left = TreeNode(4)
    obj.right = TreeNode(3)
    obj.right.left = TreeNode(2)
    obj.right.left.left = TreeNode(4)
    obj.right.right = TreeNode(4)

    # obj.traverse(obj)

    duplicate = findDuplicateSubtrees(obj)
    print("Duplicate :", duplicate)
    for i in duplicate:
        i.traverse(i)
        print()
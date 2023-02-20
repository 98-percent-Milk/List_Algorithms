from random import choices


def twoSum(nums: list[int], target: int) -> list[int]:
    """Given an array of intergers, return indices of the two numbers 
    such that they add up to a specific target.
    (Assumption: Each input would have exactly one solution,)

    Args:
        nums (list[int]): list of integers.
        target (int): Desired target (int)

    Returns:
        list[int]: Indices of the two numbers that add up to target.
    """
    # Checks in dictionary (hashTable) is in O(1) time.
    # Runtime complexity: O(n)
    # Space complexity: O(1)
    hashMap = {}  # {value: index}
    for i, v in enumerate(nums):                # O(n)
        if (diff := target - v) in hashMap:     # O(1)
            return [hashMap[diff], i]           # O(1)
        hashMap[v] = i                          # O(1)


def containsDuplicate(nums: list[int]) -> bool:
    """Given an integer array nums, return true if any value appears at least 
    twice in the array, and return false if every element is distinct.

    Args:
        nums (list[int]): list of integers.

    Returns:
        bool: True if any value appears at least twice in the array, else False
    """
    # Runtime complexity: O(n)
    # Space complexity: O(n)
    hashMap = {}
    for i, v in enumerate(nums):                 # O(n)
        if v in hashMap:                        # O(1)
            return True                         # O(1)
        hashMap[v] = i                          # O(1)
    return False


def isAnagram(forward: str, backward: str) -> bool:
    """Given two strings forward and backward, return true if backward is 
    an anagram of forward, and false otherwise.

    Args:
        forward (str): String to be checked.
        backward (str): String to check against.

    Returns:
        bool: True if backward is an anagram of forward, else False.
    """
    # Runtime complexity: O(n)
    # Space complexity: 2 * O(n)
    if len(forward) != len(backward):
        return False
    countF, countB = {}, {}

    for i in range(len(forward)):
        countF[forward[i]] = countF.get(forward[i], 0) + 1
        countB[backward[i]] = countB.get(backward[i], 0) + 1
    return countF == countB


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    """Given an array of strings strs, group the anagrams together. You can 
    return the answer in any order.

    Args:
        strs (list[str]): List of strings.

    Returns:
        list[list[str]]: List of grouped anagrams.
    """
    # Runtime complexity: O(n)
    # Space complexity: 2 * O(n)
    hashMap = {}
    for s in strs:                              # O(n)
        if (key := ''.join(sorted(s))) in hashMap:                      # O(1)
            hashMap[key].append(s)              # O(1)
        else:
            hashMap[key] = [s]                  # O(1)
    return list(hashMap.values())


def topKFrequent(nums: list[int], k: int) -> list[int]:
    """Given an integer array nums and an integer k, return the k most 
    frequent elements. You may return the answer in any order.

    Args:
        nums (list[int]): List of integers.
        k (int): Number of most frequent elements to return.

    Returns:
        list[int]: List of k most frequent elements.
    """
    # Runtime complexity: O(n)
    # Space complexity: O(n)
    hashMap = {}
    for i in nums:                              # O(n)
        hashMap[i] = hashMap.get(i, 0) + 1      # O(1)
    return [key for key, _ in sorted(hashMap.items(), key=lambda item: item[1], reverse=True)][:k]


def productExceptSelf(nums: list[int]) -> list[int]:
    """Gives an integer array nums, return an array answer such that answer[i]
    is equal to the product of all the elements of nums except nums[i].

    Args:
        nums (list[int]): list of integers.

    Returns:
        list[int]: list of products of all elements except nums[i].
    """
    # Runtime complexity: O(n)
    # Space complexity: O(1)
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):              # O(n)
        res[i] = prefix                     # O(1)
        prefix *= nums[i]                   # O(1)
    postfix = 1                             # O(1)
    for i in range(len(nums) - 1, -1, -1):  # O(n)
        res[i] *= postfix                   # O(1)
        postfix *= nums[i]                  # O(1)
    return res


def isValidSudoku(board: list[list[str]]) -> bool:
    """Checks if the given numbers on sudoku board is valid.

    Args:
        board (list[list[str]]): 2d list of strings representing sudoku board.

    Returns:
        bool: True if it is valid sudoku, else False.
    """
    # Runtime complexity: O(n)
    # Space complexity: O(n)
    row, col, box = {}, {}, {}
    for r in range(9):
        for c in range(9):
            if (num := board[r][c]) == '.':
                continue
            if ((rowKey := (r, num)) in row
                or (colKey := (c, num)) in col
                    or (boxKey := (r // 3, c // 3, num)) in box):
                return False
            row[rowKey], col[colKey], box[boxKey] = 1, 1, 1
    return True


def main():
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    isValidSudoku(board)


if __name__ == "__main__":
    main()

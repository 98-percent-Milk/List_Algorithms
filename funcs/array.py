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


def logestConsecutiveSequence(nums: list[int]) -> int:
    """given an unsorted array of integers nums, return the length of the 
    longest consecutive elements sequence.

    Args:
        nums (list[int]): list of unsorted integers.

    Returns:
        int: length of the longest consecutive elements sequence.
    """
    # Runtime complexity: O(n)
    # Space complexity: O(n)
    hashMap = set(nums)
    longest = 0
    for num in nums:
        if (num - 1) not in hashMap:
            l = 0
            while (num + (l := l + 1)) in hashMap:
                pass
            longest = [l, longest][l < longest]
    return longest


def maxArea(height: list[int]) -> int:
    """Given n non-negative integers a1, a2, ..., an , where each represents a
    line height[i] at coordinate (i, height[i]).
    Find two lines that together with the x-axis form a container, 
    such that the container contains the most water.

    Args:
        height (list[int]): vertical height of each line.

    Returns:
        int: Maximum area of the container.
    """
    # Runtime complexity: O(n)
    # Space complexity: O(1)
    lp, rp = 0, len(height) - 1
    maxArea = 0
    while lp < rp:
        maxArea = max(maxArea, min(height[lp], height[rp]) * (rp - lp))
        (lp := lp + 1) if height[lp] < height[rp] else (rp := rp - 1)
    return maxArea


def threeSum(nums: list[int], target: int = 0) -> list[list[int]]:
    """Given an integer array nums, return all the triplets that adds up to
    target value.

    Args:
        nums (list[int]): list of integers
        target (int, optional): Target value. Defaults to 0.

    Returns:
        list[list[int]]: list of triplets that adds up to target value.
    """
    nums = sorted(nums)  # Sorting will remove duplicates (results)
    triplets = []
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        lp, rp = i + 1, len(nums) - 1
        while lp < rp:
            target = a + nums[lp] + nums[rp]
            if target > 0:
                rp -= 1
            elif target < 0:
                lp += 1
            else:
                triplets += [[a, nums[lp], nums[rp]]]
                lp += 1
                while nums[lp] == nums[lp - 1] and lp < rp:
                    lp += 1
    return triplets


def nextPermutation(nums: list[int]) -> list[int]:
    """Given an array nums of distinct integers, return a next permutation
    which is lexicographically greater than the current permutation.

    Args:
        nums (list[int]): list of distinct integers.

    Returns:
        list[int]: lexically greater nextc permutation.
    """
    # If length of nums is less than or equal to 2, then reverse the list.
    if (l := len(nums)) <= 2:
        return nums.reverse()
    p = l - 1
    # Find the first index p such that nums[p] < nums[p + 1]
    while (p := p - 1) >= 0 and nums[p] >= nums[p + 1]:
        pass
    # If p < 0, then reverse the list. (Last lexicographical permutation of nums)
    if p < 0:
        return nums.reverse()
    # swap nums[p] with the smallest number greater than nums[p] to the right of p.
    for i in range(l - 1, p, -1):
        if nums[p] < nums[i]:
            nums[p], nums[i] = nums[i], nums[p]
            break
    # Reverse the list from p + 1 to the end.
    nums[p + 1:] = nums[:(p):-1]


def main():
    # [0, 1, 2, 10, 9, 5, 4]
    # [0, 1, 4, 10, 9, 5, 2]
    # [0, 1, 4, 2, 5, 9, 10]
    # Desired => [0, 1, 2, 4, 5, 9, 10]
    # nums = [0, 1, 2, 10, 9, 5, 4]
    nums = [1, 3, 2]
    l = len(nums)
    p = l - 2
    while p >= 0 and nums[p] >= nums[p + 1]:
        p -= 1
    if p < 0:
        nums.reverse()
        print(nums)
        return
    for i in range(l - 1, p, -1):
        if nums[p] < nums[i]:
            nums[p], nums[i] = nums[i], nums[p]
    nums[p + 1:] = reversed(nums[p + 1:])
    print(nums)


if __name__ == "__main__":
    main()

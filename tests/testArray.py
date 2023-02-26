import pytest
from random import choices, choice
from ArrayAndList.array import *


def test_array_twoSum():
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert twoSum([3, 2, 4], 6) == [1, 2]
    assert twoSum([3, 3], 6) == [0, 1]


def test_array_twoSum_random():
    arr = choices(range(1000), k=10)
    for _ in range(10):
        a = choice(arr)
        while (b := choice(arr)) == a:
            pass
        target = a + b
        a, b = twoSum(arr, target)
        assert arr[a] + arr[b] == target


def test_array_containsDuplicate():
    assert containsDuplicate([1, 2, 3, 1]) == True
    assert containsDuplicate([1, 2, 3, 4]) == False
    assert containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True


def test_array_isAnagram():
    assert (isAnagram("anagram", "anagram") == True)
    assert (isAnagram("dog", "god") == True)
    assert (isAnagram("rat", "car") == False)
    assert (isAnagram("Harry Potter", "harry Potter") == False)


def test_array_groupAnagrams():
    assert (groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["eat", "tea", "ate"],
        ["tan", "nat"],
        ["bat"]
    ])
    assert (groupAnagrams([""]) == [[""]])
    assert (groupAnagrams(["a"]) == [["a"]])


def test_array_topKFrequent():
    assert (topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2])
    assert (topKFrequent([1], 1) == [1])
    assert (topKFrequent([1, 2], 2) == [1, 2])


def test_array_productExceptSelf():
    assert (productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6])
    assert (productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0])
    assert (productExceptSelf([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24])
    assert (productExceptSelf([1, 2, 3, 4, 5, 6])
            == [720, 360, 240, 180, 144, 120])


def test_array_isValidSoduku():
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert (isValidSudoku(board) == True)

    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert (isValidSudoku(board) == False)


def test_array_logestConsecutiveSequence():
    assert (logestConsecutiveSequence([100, 4, 200, 1, 3, 2]) == 4)
    assert (logestConsecutiveSequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9)
    assert (logestConsecutiveSequence([1, 2, 0, 1]) == 3)
    assert (logestConsecutiveSequence([1, 3, 5, 7, 9, 11]) == 1)
    assert (logestConsecutiveSequence([10, 9, 8, 7, 6, 5, 3, 2, 1]) == 6)


def test_array_maxArea():
    assert (maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)
    assert (maxArea([1, 1]) == 1)
    assert (maxArea([4, 3, 2, 1, 4]) == 16)


def test_array_threeSum():
    assert (threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]])
    assert (threeSum([]) == [])
    assert (threeSum([0]) == [])
    assert (threeSum([0, 0, 0]) == [[0, 0, 0]])
    assert (threeSum([0, 0, 0, 0]) == [[0, 0, 0]])


def test_array_nextPermutation():
    nums = [[1, 2, 3], [1, 3, 2], [2, 1, 3],
            [2, 3, 1], [3, 1, 2], [3, 2, 1], [1], [10, 20]]
    results = [[1, 3, 2], [2, 1, 3], [2, 3, 1],
               [3, 1, 2], [3, 2, 1], [1, 2, 3], [1], [20, 10]]
    for i in range(len(nums)):
        nextPermutation(nums[i])
        assert (nums[i] == results[i])

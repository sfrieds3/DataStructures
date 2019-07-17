'''
https://leetcode.com/problems/search-in-rotated-sorted-array/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0, 1, 2, 4, 5, 6, 7] might become[4, 5, 6, 7, 0, 1, 2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4
Example 2:

Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
Output: -1
'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:


class Test:
    def testSearch():
        solution: Solution = Solution()
    assert(solution.search([4, 5, 6, 7, 0, 1, 2], 0) == 4)
    assert(solution.search([4, 5, 6, 7, 0, 1, 2], 3) == -1)


if __name__ == "__main__":
    Test.testSearch()

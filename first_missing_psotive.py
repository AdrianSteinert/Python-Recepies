from typing import List

class Solution:
    def FirstMissingPositive(self, nums: List[int]) -> int:
        found = [True] + [False] * 300
        for x in nums:
            if 0 < x < 301:
                found[x] = True  

        for i, f in enumerate(found):
            if not f:
                return i
        
        return 301


def main():
    sol = Solution()
    assert sol.FirstMissingPositive([]) == 1 
    assert sol.FirstMissingPositive([1, 2, 0]) == 3 
    assert sol.FirstMissingPositive([3, 4, -1, 1]) == 2 
    assert sol.FirstMissingPositive([7, 8, 9, 11, 12]) == 1 


if __name__ == '__main__':
    main()
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        indices = 0
        expected = sorted(heights)
        for h,e in zip(heights, expected):
            if h!=e:
                indices +=1
        return indices
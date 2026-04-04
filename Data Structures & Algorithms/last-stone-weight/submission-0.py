import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Transform the list into a max-heap in-place
        heapq.heapify_max(stones)
        
        # Keep smashing the two heaviest stones until 0 or 1 remains
        while len(stones) > 1:
            stone1 = heapq.heappop_max(stones)  # The heaviest
            stone2 = heapq.heappop_max(stones)  # The second heaviest
            
            # If they are unequal, the remaining weight goes back in
            if stone1 > stone2:
                heapq.heappush_max(stones, stone1 - stone2)
                
        # Return the last stone's weight, or 0 if none exist
        return stones[0] if stones else 0
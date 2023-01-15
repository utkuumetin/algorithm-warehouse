# Q: https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        memory = {}
        smallest = math.inf
        
        for index in range(0, len(cards)):
            value = cards[index]

            if value in memory:
                smallest = min(smallest, index - memory[value] + 1)
                
            memory[value] = index
            
        return -1 if smallest == math.inf else smallest
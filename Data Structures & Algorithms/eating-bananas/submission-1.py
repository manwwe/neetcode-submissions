class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        optimal_speed = high

        while low <= high:
            mid_speed = low + (high - low) // 2
            total_hours = 0
            for pile in piles:
                total_hours += (pile + mid_speed - 1) // mid_speed
            if total_hours <= h:
                optimal_speed = mid_speed
                high = mid_speed - 1
            else:
                low = mid_speed + 1

        return optimal_speed

        
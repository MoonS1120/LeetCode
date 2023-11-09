def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [num+extraCandies >= max(candies) for num in candies]

def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []

        for num in candies:
            result.append(num + extraCandies >= max(candies))

        return result

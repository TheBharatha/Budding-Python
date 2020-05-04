class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        distribution = list(map(lambda x: ((x+extraCandies) >= maxCandies), candies))
        return(distribution)

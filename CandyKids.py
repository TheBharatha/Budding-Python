class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)
        distribution = list(map(lambda x: ((x+extraCandies) >= maxCandies), candies))
        return(distribution)

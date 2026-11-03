class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies=max(candies)
        result=[]
        for i in range(len(candies)):
            result.append(candies[i]+extraCandies>=max_candies)
        return result
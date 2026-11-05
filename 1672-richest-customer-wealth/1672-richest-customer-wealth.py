class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth=0
        n=len(accounts)
        for i in range(n):
            if(sum(accounts[i])>max_wealth):
                max_wealth=sum(accounts[i])
        return max_wealth
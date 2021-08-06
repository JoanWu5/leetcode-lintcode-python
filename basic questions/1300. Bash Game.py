# You are playing the following game with your friend: There is a pile of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove stones.

# Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones.

# For example, if there are 4 stones, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

# Example
# Input：n = 4 
# Output：False
# Explanation：Take 1, 2 or 3 first, the other party will take the last one

class Solution:
    """
    @param n: an integer
    @return: whether you can win the game given the number of stones in the heap
    """
    def canWinBash(self, n):
        # Write your code here
        return n % 4 != 0
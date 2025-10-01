class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = 0
        emptyBottles = 0

        while numBottles != 0:
            count += numBottles
            emptyBottles += numBottles
            numBottles = emptyBottles // numExchange #finds the bottle which were used
            emptyBottles = emptyBottles % numExchange
        return count

        
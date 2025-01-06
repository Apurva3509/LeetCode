class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        # for every triplet we check if any values in that triplet is >= the target triplet at any index
        # If so, that triplet is useless to us as when we tak max, we cannot achieve target
        # for all the remaining triplets we see if we have the element at a particular index in any of the 
        # triplet, if so for all 3 positions we can guarantee that we can form the target

        good = set() # add indices of good triplets posiyions, i.e index 1, 2, 3; if len =3 we return true

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for i, v in enumerate(t):
                if v == target[i]: # if the value in triplet is in target, we add to good set
                    good.add(i)

        return len(good) == 3
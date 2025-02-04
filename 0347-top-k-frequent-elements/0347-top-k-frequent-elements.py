class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # hmap= {}
        
        # # Approach 1: Hashmap and then sort hashmap according to key and return it
        # for i, n in enumerate(nums):
        #     if n in hmap:
        #         hmap[n]+=1
        #     else:
        #         hmap[n]=1
        # return [key for key, _ in sorted(hmap.items(), key=lambda x: x[1], reverse=True)[:k]]

        # Approach 2: Use a hashmap to count values and then initialize and aray with length of given array
        # Idea being that the index will serve as count and the values on index will be list of elements with that count
        # we make an array of length of given list becasue the count of any element cannot be > than the size of given list

        count = {}
        freq = [[] for i in range(len(nums) +1)]

        for n in nums:
            count[n] = 1 + count.get(n,0) #counting occurance of n in nums and updating the count accordingly; count.get(n,0) gives total occurances of n and if nil adds 0
            
        for n,c in count.items(): #n,c are key value pair in the hashmap count
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1): #in reverse order of length of array so -1 and until 0 index
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
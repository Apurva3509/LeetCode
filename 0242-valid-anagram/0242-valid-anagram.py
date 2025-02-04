class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dicx1={}
        dicx2={}

        for i in s:
            if i in dicx1:
                dicx1[i]+=1
            else:
                dicx1[i]=1

        for i in t:
            if i in dicx2:
                dicx2[i]+=1
            else:
                dicx2[i]=1

        if dicx1==dicx2:
            return True
        else:
            return False
        
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longPrefix = strs[0]
        for i in range(len(strs)-1):
            longPrefix = self.compareStrings(longPrefix,strs[i+1])
            #print(longPrefix)
            if longPrefix == "":
                return ""
            else:
                continue
        return longPrefix

    def compareStrings(self,L1:str,L2:str)->str:
        k = min(len(L1),len(L2))
        #print(k)
        output = ""
        if k <= 0 :
            return ""
        for i in range(k):
           if L1[i]==L2[i]:
               output += L1[i]
           else:
               return output
        return output


soln = Solution()
str= ["cfr","car"]
#print(soln.compareStrings("hi","heee"))
print(soln.longestCommonPrefix(str))
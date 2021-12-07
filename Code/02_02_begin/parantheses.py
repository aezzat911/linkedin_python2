class Solution:
    def isValid(self, s: str) -> bool:
        if  len(s)%2 > 0 :
            print ("odd")
            return False
        for i in range(len(s)//2):
            if self.isSuitable(s[i],s[-1*(i+1)]):
                continue
            else:
                return False
        return True

    def isSuitable(self,str1,str2):
        if (str1 == "(" and str2 == ")" ) or (str1 == "{" and str2 == "}") or (str1 == "[" and str2 == "]") :
            return True
        else:
            return False


input = "()[]{}"
soln = Solution()
#output = soln.isSuitable("(","]")
output = soln.isValid(input)

print (output)



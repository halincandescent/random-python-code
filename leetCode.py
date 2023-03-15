import math 
#numList = [5,4,2,3]

from itertools import combinations


##
class Solution:
    ##
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 1 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]
    ##
    def isPalindrome(self, num : int) -> bool:
        # 9 
        string = str(num)
        length = len(string)
        firstHalf = '' 
        if length%2 == 0:
            halfIndice = length//2 - 1
            i = 0
            while i < length//2: 
                firstHalf = firstHalf + string[i]
                i = i + 1
            j = len(firstHalf) - 1
            strPal = ''
            while j > -1:
                strPal = strPal + firstHalf[j]
                j = j - 1
            return int(strPal)==num
        else:
            middleIndice = length//2
            firstHalf = ''
            i = 0
            while i < middleIndice:
                firstHalf = firstHalf + string[i]
                i = i + 1
            strPal = firstHalf + string[middleIndice]
            j = len(firstHalf)- 1
            while j > - 1:
                strPal = strPal + firstHalf[j]
                j = j-1
            return int(strPal)==num

##Symbol       Value
##I             1
##V             5
##X             10
##L             50
##C             100
##D             500
##M             1000
##I can be placed before V (5) and X (10) to make 4 and 9. 
##X can be placed before L (50) and C (100) to make 40 and 90. 
##C can be placed before D (500) and M (1000) to make 400 and 900.
## 1 can be placed before V (5) and X (10) to make 4 and 9. 
## 10 can be placed before L (50) and C (100) to make 40 and 90. 
## 100 can be placed before D (500) and M (1000) to make 400 and 900.    

    def romanToInt(self, s:str) -> int:
        # 13
        romanSplit = []
        romanDictionary = {'I':1,'V':5,'X':10,'L':50,
                         'C':100,'D':500,'M':1000}
        for i in s:
            romanSplit.append(i)
        # replace numerals with numbers
        i = 0
        while i < len(romanSplit):
            numeral = romanSplit[i]
            number = romanDictionary[numeral]
            romanSplit[i] = number
            i = i + 1
            
        integer = 0
        i = 0
        while i < len(romanSplit):
            # end 
            if i == len(romanSplit) - 1:
                pass
            else:
                if romanSplit[i] > romanSplit[i +1]:
                    integer = integer + romanSplit[i]
                    i = i + 1
                elif romanSplit[i] == romanSplit[i+1]:
                    integer = integer + romanSplit[i]
                    i = i + 1
                elif romanSplit[i] < romanSplit[i+1]:
                    # subtraction rules 
                    
                    pass
    ### 13 not done
                
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # 14 
        if len(strs)==0:
            return ''
        if len(strs)==1:
            return ''
        else:
            commonStr = ''
            i = 0 # iterate over letters in words
            while i < len(min(strs, key=len)) - 1:
                j = 0 # iterate over list of words
                while j < len(strs)-1:
                    if strs[j+1][i] == strs[j][i]:
                        pass
                    else: 
                        return commonStr
                    j = j + 1 
                commonStr = commonStr + strs[j][i]
                i = i + 1

            return commonStr

    def isValid(self, s: str) -> bool: ### didn't do 
        # 20
        openBracket = '('
        closeBracket = ')'
        openSquare = '['
        closeSquare = ']'
        openCurly = '{'
        closeCurly = '}'
        pass

    def mergeTwoLists(self, list1: [list], list2: [list]) -> [list]:
        # 21
        listNew = []
        if len(list1)>len(list2):
            diff = len(list1) - len(list2)
            i = 0
            while i < len(list2):
                listNew.append(list1[i])
                listNew.append(list2[i])
                i = i + 1
            # make sure indices are right
            listNew = listNew + list1[len(list2):]
            
            
        elif len(list2)>len(list1):
            diff = len(list2)-len(list1)
            i = 0
            while i < len(list1):
                listNew.append(list1[i])
                listNew.append(list2[i])
                i = i + 1
            # make sure indices are right
            listNew = listNew + list2[len(list1):]
        else:## as if equal
            i = 0
            while i <len(list1):
                listNew.append(list1[i])
                listNew.append(list2[i])
                i = i + 1
                
        return listNew

    def removeDuplicates(self, nums: list[int]) -> int:
        #listex = [0,0,1,1,1,2,2,3,3,4]
        # 26
        i = 0
        currInt = 9999999
        kCount = 0 
        while i < len(nums):
            tempInt = nums[i]
            if tempInt == currInt:
                nums[i] = 999
            else:
                currInt = tempInt
                kCount = kCount + 1 
            i = i+1
        nums.sort()
        ## could use a code to to make a number and check if in list prior
        ## to be extra fancy 
        return kCount 
                

    def removeElement(self, nums: list[int], val: int) -> int:
            # 27
            ## is just question 26 with a modification
        pass
    def searchInsert(self, nums: list[int], target: int) -> int:
            # 35
            ##Given a sorted array of distinct integers and
            ##a target value, return the index if the target is found.
            ##If not, return the index where it would
            ##be if it were inserted in order.
            i = 0
            while i < len(nums):
                tempNum = nums[i]
                if tempNum == target:
                    return i
                else:
                    if tempNums > target and i > 0:
                        return i-1
                    else:
                        i = + 1
        
    def lengthOfLastWord(self, s: str) -> int:
            # 58 
            # input = "   fly me   to   the moon "
            listString = s.split()
            return len(listString[-1])

    def plusOne(self, digits: list[int]) -> list[int]:
            # 66
            # Input: digits = [4,3,2,1]
##            Output: [4,3,2,2]
##            Explanation: The array represents the integer 4321.
##            Incrementing by one gives 4321 + 1 = 4322.
##            Thus, the result should be [4,3,2,2].
            # Input = [0,9]
            # Output = [1,0] 
            i = 0
            strInt = ''
            while i < len(digits):
                strInt = strInt + digits[i]
                i = i + 1
            #add 1
            plusOneInt = int(strInt) + 1
            strInt = str(plusOneInt)
            digitPlusOne = []
            i = 0
            while i < len(strInt):
                integer = int(strInt[i])
                digitPlusOne.append(integer)
                i = i + 1
            return digitPlusOne

##     def addBinary(self, a: str, b: str) -> str:
##        #67
##        # 0 + 0 = 0.
##        # 0 + 1 = 1.
##        # 1 + 0 = 1.
##        # 1 + 1 =10.
##
##        c = ''
##        if len(a) > len(b):
##            pass
##        elif len(b) > len(a):
##            pass
##        elif len(a)==len(b):
##            pass

    def removeDuplicates(self, nums: list[list[int]]) -> list[list[int]]:
        pass 


    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ## finds a sum of three digits from numsList that add up to 0
        ## no duplicates
        # Input: nums = [-1,0,1,2,-1,-4]
        # Output: [[-1,-1,2],[-1,0,1]]
        # no repeat indices

        # find group of three permutations
        listThreeSum = []
        groupThreePermutations = list(combinations(nums,3))
        for group in groupThreePermutations:
            summation = []
            i = 0
            while i < len(group):
                summation.append(group[i])
                i = i + 1
            if sum(summation) == 0:
                listThreeSum.append(summation)
        ## needs to remove duplicates
        ## sort and then remove duplicates right? 
        return listThreeSum

    def permute(self, nums: list) -> list[list[int]]:
        pass
            
                    

    
        
                    
#numList = [5,4,2,3]
#targ = 7
##number = 12221
if __name__=='__main__':
    roman = 'LVI'
    stringList = ['cat','car','capital'] 
    s = Solution() 
    #print(s.romanToInt(roman))
    #print(s.longestCommonPrefix(stringList))
    #listex = [0,0,1,1,1,2,2,3,3,4]
    #print(s.removeDuplicates(listex))
    #print(listex)
    listEx = [-1,0,1,2,-1,-4]
    print(s.threeSum(listEx))

        
        
    
        
        





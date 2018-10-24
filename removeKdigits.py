class Solution(object):
    def remove1digit(self, index, num, k):
        
        if len(num) == k:
            return 0, "0"
        
        change = False
        if index == 0:
            index = 1
            
        for j in range(index - 1, len(num) - 1):
            if num[j] > num[j+1]:
                num = num[:j] + num[j+1:]
                change = True             
                break
        if j == len(num) - 2 and change == False:
            if num[-1] >= num[-2]:
                num = num[:-1]
            
        num = str(int(num))
        return j, num
        
    def removeKdigits(self, num, k):      
        if len(num) == k:
            return "0"
        index = 0
        for i in range(0,k):
            index, num = self.remove1digit(index,num,k-i)
        
        return num
            
            
        """
        :type num: str
        :type k: int
        :rtype: str
        """
# time limit exceeded: O(n^k)

#by discussion      
class Solution:
    def removeKdigits(self, nums, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for x in nums:
            while stack and x < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            stack.append(x)
        for i in range(k):stack.pop()
        while stack and stack[0] == '0': del stack[0]
        if not stack:stack.append('0')
        return ''.join(stack)


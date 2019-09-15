class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ")":
                stack.append(i)
            else:
                tmp = ""
                while (stack[-1] != "("):
                    tmp = tmp + stack.pop()
                stack.pop()
                for j in tmp:
                    stack.append(j)
        
        return "".join(stack)
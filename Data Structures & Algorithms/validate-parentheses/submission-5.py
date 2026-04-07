class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        for i in range(len(s)):
            if s[i] in '{[(':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                stack_top = stack.pop()
                if (s[i] == '}' and stack_top == "{" 
                or s[i] == ')' and stack_top == "(" 
                or s[i] == ']' and stack_top == "[") :
                    continue
                return False
        
        if stack:
            return False
        return True
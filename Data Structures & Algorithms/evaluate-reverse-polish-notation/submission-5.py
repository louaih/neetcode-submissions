class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque()
        ops = '+-*/'
        for t in tokens:
            if t in ops:
                op2 = stack.pop()
                op1 = stack.pop()
                if t == '/':
                    stack.append(str(int(int(op1) / int(op2))))
                else:
                    stack.append(str(eval(op1+t+op2)))
            else:
                stack.append(t)

        return int(stack[-1])
        
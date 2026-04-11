import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numstack = []
        opstack = []
        oplist = {"+", "-", "*", "/"}
        for i in tokens:
            if i not in oplist:
                numstack.append(int(i))
            else:
                print(numstack)
                right = numstack.pop()
                left = numstack.pop()
                if i == "+":
                    numstack.append(left + right)
                elif i == "-":
                    numstack.append(left - right)
                elif i== "*":
                    numstack.append(left * right)
                else:
                    numstack.append(math.trunc(left/right))
        return numstack[0]
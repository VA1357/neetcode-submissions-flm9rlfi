class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #just use a stack for numbers every time u see an op take last two numbers apply and add back to stack
        #the issue is the truncate to zero, truncate implies use of math.truncate() which gets rid of decimal altogether, otherwise either your negatives round down or ur positives round up if u try an alternate
        numstack = []
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
                    numstack.append(int(left/right))
        return numstack[0]
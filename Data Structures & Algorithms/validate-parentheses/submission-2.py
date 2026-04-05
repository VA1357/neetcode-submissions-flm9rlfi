class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==0:
            return False
        stack = []
        parmap = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            else:
                if not stack:
                    return False
                curr = stack.pop()
                if curr != parmap[i]:
                    return False
        if len(stack)!=0:
            return False
        return True
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if len(s) < 1:
            return True
        
        ''' if odd then automatically false'''
        if len(s) % 2 != 0:
            return False
        
        bracket_dict = {
            '}': '{',
            ')': '(',
            ']': '[',
        }
        
        stack = []
        
        for char in s:
            if char in bracket_dict:
                end = stack.pop() if stack else "?"
                
                if bracket_dict[char] != end:
                    return False
            else:
                stack.append(char)
                
        return True if len(stack) == 0 else False

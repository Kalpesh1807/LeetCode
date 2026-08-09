# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for breacket in s:
            if breacket == "(" or breacket == "{" or breacket =="[" :
                stack.append
            else:
                if len(stack) == 0:
                    return False
                ch = stack.pop()
                if( 
                    (breacket ==")" and ch =="(" )
                    or (breacket == "]" and ch == "[")
                    or (breacket == "}" and ch == "{")
                ):
                    continue
                else:
                    return False
        return len(stack == 0)


    
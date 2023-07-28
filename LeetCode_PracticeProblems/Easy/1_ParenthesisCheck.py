"""_Problem Statement : 
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
    
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        valid = {')':'(','}':'{',']':'['}
        for i in s:
            if i in ['(','{','[']:
                stk.append(i)
                continue
            if len(stk) >0 and stk[-1] == valid[i]:
                stk.pop()
                continue
            else:
                return False
        if stk == []:
            return True
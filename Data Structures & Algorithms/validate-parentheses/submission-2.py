class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                if char == ")":
                    if not stack:
                        return False
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                
                if char == "}":
                    if not stack:
                        return False
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False

                if char == "]":
                    if not stack:
                        return False
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
        if stack:
            return False
        return True

                
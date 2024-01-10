def isValid(self, s):
        stack = []

        for char in s:
            if char in ['(','[', "{"]:
                stack.append(char)
            else:
                if stack:
                    pop = stack.pop()
                    if  char == ')' and pop == '(' or \
                        char == ']' and pop == '[' or \
                        char == '}' and pop == '{':
                        continue
                    else:
                        return False
                else:
                    return False

        return not stack
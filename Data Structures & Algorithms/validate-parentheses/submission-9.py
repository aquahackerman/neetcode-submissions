class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_brackets = "([{"
        print("hi")
        for i, letter in enumerate(s):
            
            if len(stack) == 0:
                stack.append(letter)
            elif letter in opening_brackets:
                stack.append(letter)
            else:
                print(stack[-1])
                if letter == "}" and stack[-1] == "{":
                    stack.pop()
                elif letter == "]" and stack[-1] == "[":
                    stack.pop()
                elif letter == ")" and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

                    
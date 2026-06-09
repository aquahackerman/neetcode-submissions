class Solution:
    @staticmethod
    def is_int(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if Solution.is_int(token):   # ✅ correct call
                stack.append(int(token))
            else:
                n1 = stack.pop()
                n2 = stack.pop()

                if token == "+":
                    stack.append(n2 + n1)
                elif token == "-":
                    stack.append(n2 - n1)
                elif token == "*":
                    stack.append(n2 * n1)
                elif token == "/":
                    stack.append(int(n2 / n1))  # LeetCode-style truncation

        return stack[-1]

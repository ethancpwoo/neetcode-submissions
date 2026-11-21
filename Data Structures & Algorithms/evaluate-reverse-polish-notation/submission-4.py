class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for token in tokens:
            if token == '+':
                n1 = s.pop()
                n2 = s.pop()
                s.append(n1+n2)
            elif token == '-':
                n1 = s.pop()
                n2 = s.pop()
                s.append(n2-n1)
            elif token == '*':
                n1 = s.pop()
                n2 = s.pop()
                s.append(n1*n2)
            elif token == '/':
                n1 = s.pop()
                n2 = s.pop()
                s.append(int(n2/n1))
            else:
                s.append(int(token))
        return s[0]
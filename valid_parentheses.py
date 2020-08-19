# https://www.codewars.com/kata/52774a314c2333f0a7000688/

def valid_parentheses(string):
    stack = []
    for token in string:
        if token == "(":
            stack.append(token)
        elif token == ")":
            if len(stack) != 0:
                stack.pop()
            else:
                return False
    return len(stack) == 0


print(valid_parentheses(")test"))

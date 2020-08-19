# kata https://www.codewars.com/kata/5277c8a221e209d3f6000b56

def valid_braces(string):
    match = {")": "(", "]": "[", "}": "{"}
    stack = []
    for token in string:
        if token in match.keys():
            if len(stack) == 0 or stack.pop() != match[token]:
                return False
        else:
            stack.append(token)
    return len(stack) == 0


print(valid_braces("()"))

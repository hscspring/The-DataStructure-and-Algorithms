def is_valid(s: str) -> bool:
    stack = []
    for i in s:
        if i in ["(", "[", "{"]:
            stack.append(i)
        else:
            if not stack or not peak(stack.pop(), i):
                return False
    if stack:
        return False
    return True

def peak(s1, s2):
    if s1 == "(":
        return s2 == ")"
    if s1 == "[":
        return s2 == "]"
    if s1 == "{":
        return s2 == "}"




inputs = [
    ["()", "()[]{}", "(]", "([)]", "{[]}", "["],
    [True, True, False, False, True, False]
]


for i in range(len(inputs[0])):
    inp = inputs[0][i]
    res = inputs[1][i]
    assert is_valid(inp) == res
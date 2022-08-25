class Stack:

    def __init__(self):
        self.data = []

    def push(self, v) -> None:
        self.data.append(v)

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def pop(self) -> int:
        if self.is_empty():
            print("error")
            return
        return self.data.pop()

    def top(self) -> int:
        if self.is_empty():
            print("error")
            return
        return self.data[-1]

    def size(self) -> int:
        return len(self.data)


stack = Stack()
print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)

print(lines)

for inp in lines:
    if inp.startswith("push"):
        _, v = inp.split()
        stack.push(int(v))
    elif inp.startswith("pop"):
        v = stack.pop()
        if v:
            print(v)
    elif inp.startswith("top"):
        v = stack.top()
        if v:
            print(v)

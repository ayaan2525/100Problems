"""
Remove all duplicate adjacent characters
i/p: baab > o/p: ""
i/p: aaabccddd > o/p: abd
"""

input_str = input("Enter string: ")
stack = []
top = 0

for ch in input_str:
    if top > 0 and stack[top - 1] == ch:
        stack.pop()
        top -= 1
    else:
        stack.append(ch)
        top += 1

print("".join(stack))

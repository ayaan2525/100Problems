# Reverse Polish Notation Evaluator

input_str = input("Enter RPN expression (e.g., 2 1 + 3 *): ")

tokens = input_str.strip().split()
stack = []

for token in tokens:
    if token in ['+', '-', '*', '/']:
        operand_B = stack.pop()
        operand_A = stack.pop()
        if token == '+':
            result = operand_A + operand_B
        elif token == '-':
            result = operand_A - operand_B
        elif token == '*':
            result = operand_A * operand_B
        elif token == '/':
            result = int(operand_A / operand_B)
        stack.append(result)
    else:
        stack.append(int(token))

print("Result:", stack.pop())

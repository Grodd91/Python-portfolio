def calculate(s):
    stack = []
    num = 0
    sign = 1
    result = 0

    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '+':
            result += sign * num
            num = 0
            sign = 1
        elif char == '-':
            result += sign * num
            num = 0
            sign = -1
        elif char == '(':
            stack.append((result, sign))
            result = 0
            sign = 1
        elif char == ')':
            prev_result, prev_sign = stack.pop()
            result = prev_result + prev_sign * result

    return result + sign * num

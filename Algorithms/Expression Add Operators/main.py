def add_operators(num, target):
    def backtrack(index, prev_operand, current_operand, value, path):
        if index == len(num):
            if value == target:
                result.append(path)
            return

        for i in range(index, len(num)):
            if i != index and num[index] == '0':
                break

            next_operand = int(num[index:i + 1])
            if index == 0:
                backtrack(i + 1, next_operand, next_operand, next_operand, str(next_operand))
            else:
                backtrack(i + 1, next_operand, current_operand + next_operand, value + next_operand, path + '+' + str(next_operand))
                backtrack(i + 1, -next_operand, current_operand - next_operand, value - next_operand, path + '-' + str(next_operand))
                backtrack(i + 1, current_operand * next_operand, current_operand * next_operand, value - current_operand + current_operand * next_operand, path + '*' + str(next_operand))

    result = []
    backtrack(0, 0, 0, 0, '')
    return result

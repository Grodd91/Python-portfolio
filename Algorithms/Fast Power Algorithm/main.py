def power(base, exponent):
    if exponent == 0:
        return 1
    result = power(base, exponent // 2)
    if exponent % 2 == 0:
        return result * result
    else:
        return result * result * base

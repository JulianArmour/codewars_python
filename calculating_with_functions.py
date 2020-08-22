import operator


def number(fn, num):
    if fn:
        return fn(num)
    return num


def zero(fn=None):
    return number(fn, 0)


def one(fn=None):
    return number(fn, 1)


def two(fn=None):
    return number(fn, 2)


def three(fn=None):
    return number(fn, 3)


def four(fn=None):
    return number(fn, 4)


def five(fn=None):
    return number(fn, 5)


def six(fn=None):
    return number(fn, 6)


def seven(fn=None):
    return number(fn, 7)


def eight(fn=None):
    return number(fn, 8)


def nine(fn=None):
    return number(fn, 9)


def bin_op(operator, second_operand):
    return lambda first_operand: operator(first_operand, second_operand)


def plus(num):
    return bin_op(operator.add, num)


def minus(num):
    return bin_op(operator.sub, num)


def times(num):
    return bin_op(operator.mul, num)


def divided_by(num):
    return bin_op(operator.floordiv, num)

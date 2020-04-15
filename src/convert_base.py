DIGITS = "0123456789abcdef"


def convert_base_stack(decimal_number, base):
    remainder_stack = []

    while decimal_number > 0:
        remainder = decimal_number % base
        remainder_stack.append(remainder)
        decimal_number = decimal_number // base

    new_digits = []
    while remainder_stack:
        new_digits.append(DIGITS[remainder_stack.pop()])

    return "".join(new_digits)


def convert_base_rec(decimal_number, base):
    if decimal_number < base:
        return DIGITS[decimal_number]

    return convert_base_rec(decimal_number // base, base) + DIGITS[decimal_number % base]

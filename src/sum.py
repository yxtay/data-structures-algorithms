def sum_iter(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total


def sum_rec(numbers):
    if len(numbers) == 0:
        return 0

    return numbers[0] + sum_rec(numbers[1:])

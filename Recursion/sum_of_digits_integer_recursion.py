def sum_of_digits(num):
    assert int(num) == num and num >= 0, 'the number has to be positive integer'
    if num == 0:
        return 0
    else:
        return int(num % 10) + sum_of_digits(num // 10)


print(sum_of_digits(4.11))




def factorial(n):
    assert n>=0 and int(n)==n,'the number must be positive only'
    if n < 1:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(4))
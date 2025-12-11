def mortal_fib(n, m):
    ages = [0]*m
    ages[0] = 1

    for _ in range(1, n):
        newborns = sum(ages[1:])
        ages = [newborns] + ages[:-1]

    return sum(ages)

print(mortal_fib(91, 16))

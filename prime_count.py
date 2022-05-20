def prime_count(start, end):

    count = 0
    if end < 2:
        return count
    if start < 2:
        start = 2

    for number in range(start, end + 1):
        flag = True
        for divisor in range(2, number):
            if number % divisor == 0:
                flag = False
                break
        if flag:
            count += 1
    return count


print(prime_count(10, 30))  # output is 6
print(prime_count(11, 29))  # output is 6
print(prime_count(20, 22))  # output is 0
print(prime_count(1, 1))  # output is 0
print(prime_count(5, 5))  # output is 1
print(prime_count(6, 2))  # output is 0
print(prime_count(-10, 6))  # output is 3

def guthrie(n):
    flag = True
    result = [n]
    while flag:
        if n % 2 == 0:
            n = int(n / 2)
            result.append(n)
        else:
            n = int(n * 3 + 1)
            result.append(n)

        if n == 1:
            flag = False

    return result


print(guthrie(7))  # output is [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

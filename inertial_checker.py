def inertial_checker(arr):

    odd_list = []
    even_list = []
    max_value = max(arr)
    for number in arr:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)
    odd_list.sort()
    even_list.sort()
    if max_value % 2 != 0:
        return 0
    elif len(odd_list) < 1:
        return 0
    elif len(even_list) > 1:
        for i in range(len(even_list) - 2, -1, -1):
            if even_list[i] != max_value:
                if odd_list[0] < even_list[i]:
                    return 0
                else:
                    return 1
            else:
                return 1

    else:
        return 1


print(inertial_checker([1]))  # output is 0
print(inertial_checker([2]))  # output is 0
print(inertial_checker([1, 2, 3, 4]))  # output is 0
print(inertial_checker([1, 1, 1, 1, 1, 1, 2]))  # output is 1
print(inertial_checker([2, 12, 12, 4, 6, 8, 11]))  # output is 1
print(inertial_checker([-2, -4, -6, -8, -11]))  # output is 0


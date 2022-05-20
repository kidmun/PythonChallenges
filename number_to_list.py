def convert(number):

    string_number = str(number)
    result = []

    for num in string_number:
        result.append(int(num))

    return result


print(convert(12))  # output is [1,2]
print(convert(123))  # output is [1,2,3]
print(convert(1))  # output is [1]
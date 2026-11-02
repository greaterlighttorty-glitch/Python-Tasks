def sum_of_tuple(ite):
    return item[0] + item[1]

def confirmation(item):
    return sum_of_tuple(item) > 5

numbers = [(1, 2), (3, 4), (5, 6)]
result = list(filter(sum_confirmation, numbers))
print(result)




def sum_calculation(data):
    numbers = []

    for item in data:
        if item.isdigit():
            numbers.append(int(item))
    return sum(numbers)

data = ['123', '456', '789', 'abc', 'def']
print(sum_calculation(data))

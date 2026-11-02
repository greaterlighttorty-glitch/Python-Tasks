def Uppercase(word):
    return words.upper()
words = ['python', 'java', 'c++']
result = list(map(Uppercase, words))
print(result)



def square_numbers(number):
    return number * number
numbers = range(1, 11)
result = list(map(square_numbers, numbers))
print(result)



def Capitalize(name):
    return name[0].upper() + name[1:]
names = ['john', 'mary', 'steve']
result = list(map(Capitalize, names))
print(names)



def percent(price):
    return price * (price / 10)
prices = [100, 200, 300]
result = list(map(percent, prices))
print(result)





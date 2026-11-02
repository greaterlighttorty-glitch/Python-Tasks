from functools import reduce


def sum(first_number, second_number):
    return first_number + second_number
number = range(1, 51)
result = reduce(su, number)
print(result)


def find(first_number, seccond_number):
    if first_number > second_number:
        return first_number
    else:
        return second_number

numbers = [3, 5, 9, 2, 8]
maximum = reduce(find, numbers)

print("Maximum number:", maximum)



def concatenate(first_word, second_word):
    return first_word + " " + second_word

words = ['I', 'love', 'Python']
sentence = reduce(concatenate, words)

print("words: ", sentence)



def square_numbers(number):
    return number ** 2

def multiply(number_one, number_two):
    return number_one * number_two

numbers = [1, 2, 3, 4]

square = list(map(square_numbers, numbers))
product = reduce(multiply, square)

print("the product of sguare: ", product)

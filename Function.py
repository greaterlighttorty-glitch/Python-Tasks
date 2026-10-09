def the_word(word):
    the_length = len(word)
    return the_length

def character(word):
    if len(word) < 2:
        return ' '
    return word[:2] + word[-2:]
    

def add_ing(word):
    if(len(word) > 3):
        return word + 'ing'
        
    if(len(word) > 3):
        return word + 'ly'
    else:
        return word
        
def longest_word(words):
    longest = " "
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest, len(longest)
    
the_list = ["welcome","out","weather","mobile","breakfast","journey"] 
result_word, result_length = longest_word(the_list) 


def odd_index(word):
    result = ""
    for character in range(len(word)):
        if character % 2 == 1:
            result += word[character]
    return result


def minimum_numbers(numbers):
    smallest = numbers[0]
    for the_number in numbers:
        if the_number < smallest:
            smallest = the_number
    return smallest
                
def maximum_numbers(numbers):
    largest = numbers[0]
    for the_number in numbers:
        if the_number > largest:
            largest = the_number
    return largest
    
    
def repeated(word, number):
    if type(number) == float:
        return word
        
    result = ""
    for index in range(number):
        result += word
    return result

def square(numbers):
    result = []
    for the_numbers in numbers:
        result.append(the_numbers * the_numbers)
    return result
    
def sum_of_square(numbers):
    total = 0
    for the_numbers in numbers:
        total += (the_numbers * the_numbers)
    return total
  


print(the_word('introduction'))

print(character('semicolon'))
print(character('on'))
print(character('o'))

print(add_ing('abc'))

print(result_word, result_length)

print(odd_index('semicolon'))      

print(minimum_numbers([8, 4, 9, 2, 5, 7,3]))  

print(maximum_numbers([8, 4, 9, 2, 5, 7,3])) 

print(repeated('hello', 3))
print(repeated('hi', 4.5))

print(square([2, 3, 4, 5, 7]))

print(sum_of_square([2, 3, 4, 5, 7]))

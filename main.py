""" https://www.youtube.com/watch?v=twxE0dEp3qQ """

""" One """ 
values = []
for x in range(10):
    values.append(x)

# USing list comprehension:
values = [x for x in range(10)]
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


""" Two """
evens = []
for number in range(50):
    is_Even = number % 2 == 0
    if is_Even:
        evens.append(number)

# USing list comprehension:
evens = [number for number in range(50) if number % 2 == 0]
# Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]


""" Three """
options = ["any", "albany", "apple", "world", "hello", "","ay"]
valid_strings =[]
for  string in options:
    if len(string) <= 1:
        continue
    
    if string[0] != "a":
        continue

    if string[-1] != "y":
        continue

    valid_strings.append(string)


#Using Comprehensions:
valid_strings = [
    string
    for string in options
    if len(string) >= 2
    if string[0] == "a"
    if string[-1] == "y"
]
# Output: ['any', 'albany', 'ay']


""" Four """
matrix = [[1,2,3], [4,5,6], [7,8,9]]
flattened = []

for row in matrix:
    for num in row:
        flattened.append(num)


# Using Comprehension:
flattened = [num for row in matrix for num in row]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


""" Five """
categories = []

for number in range(10):
    if number % 2 == 0:
        categories.append("Even")
    else:
        categories.append("odd")


# USing Conprehensions:
categories = ["Even" if number % 2 == 0 else "odd" for number in range(10)]
# Output: ['Even', 'odd', 'Even', 'odd', 'Even', 'odd', 'Even', 'odd', 'Even', 'odd']


""" Six """
import pprint
printer = pprint.PrettyPrinter()

lst = []

for a in range(5):
    l1 = []
    for b in range(5):
        l2 = []
        for num in range(5):
            l2.append(num)
        l1.append(l1)

    lst.append(l1)

printer.pprint(lst)
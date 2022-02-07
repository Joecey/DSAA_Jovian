import math

print("packages imported")

# Problem: Alice has some cards with numbers written on them. She arranges the cards in decreasing order,
# and lays them out face down in a sequence on a table.
# She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
# Write a function to help Bob locate the card.

# WRITE MAIN SOLUTION FUNCTION HERE
def locate_card(cards, query):
    pass

# TESTS
# cards does not contain query
tests = []
# Dictionaries (you can do subdictionary inside a dictionary)
# Example test
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
})

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

# query not in cards
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})


# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

# Test solution here
# print(tests)
tests_num = len(tests)

for i in range(0, tests_num):
    print(locate_card(**tests[i]['input']) == tests[i]['output'])

# print(locate_card(**test['input']) == test['output'])
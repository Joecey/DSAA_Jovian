import math
import time
# import datetime
# start_time = time.process_time()

print("packages imported")

# Problem: Alice has some cards with numbers written on them. She arranges the cards in decreasing order,
# and lays them out face down in a sequence on a table.
# She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
# Write a function to help Bob locate the card.

# WRITE MAIN SOLUTION FUNCTION HERE
def locate_card_binary(cards, query):
    # O(log N) time complexity

    # check if cards is not empty
    if cards == []:
        return -1

    else:

        # setup lo and hi values (far left and far right initial parameters
        lo, hi = 0, len(cards)

        # while lo is less than or equal to high
        while lo <= hi:
            mid_pos = (lo+hi) // 2 # integer division
            mid_number = cards[mid_pos]

            # check where mid number is relative to query
            if mid_number == query:
                return  mid_pos
            elif mid_number < query:    # not on the right side of mid (AND also not mid)
                hi = mid_pos - 1
            elif mid_number > query:
                lo = mid_pos + 1

        # if none of the above is not possible
        return -1


def locate_card_linear(cards, query):
    # O(N) time complexity
    position = 0

    # check if cards is empty
    if cards == []:
        return -1

    else:
    # loop for repition
        while True:
            if cards[position] == query:

                # answer found
                return position

            # increment
            position += 1

            # if reached end but not found, return -1
            if position == len(cards):

                return -1

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
# start_time = datetime.datetime.now()
tests_num = len(tests)

for i in range(0, tests_num):
    # print(locate_card_linear(**tests[i]['input']))
    # print(locate_card_linear(**tests[i]['input']) == tests[i]['output'])

    print(locate_card_binary(**tests[i]['input']))
    print(locate_card_binary(**tests[i]['input']) == tests[i]['output'])


# print(locate_card(**test['input']) == test['output'])

# Check execution time
# test 2
print("--- %s seconds ---" % (time.process_time()))

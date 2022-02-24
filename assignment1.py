# assignment 1 from jovian

# jovian project can be found here: https://jovian.ai/joecey/python-binary-search-assignment

import jovian
import math
import time

print("packages imported")

project='python-binary-search-assignment'
jovian.commit(project=project, privacy='secret', environment=None)

# sorted list = ascending order
# rotating a list = taking number at end of list and putting it to the front

# for a sorted list and a given list, figure out how many rotations it took to
# turn the sorted list into the given list

# input nums = array of given list
# output rotations = number of rotations it took

# if array is not sorted, there will always be a number larger than the original number

# function --> take given list
    # test if array is sorted
    # rotations = 0
    # array = not sorted

        # while array not sorted
        # get middle number and take left section (make note of middle number)
            # set test = 0
            # set left to index 0, set right to index (middle - 1)

            # if left < right
                # get middle number of left side
                # if new middle < original middle
                    # continue

                # else
                    # bring index 0 to end (given.sort(key=given[0].__eq__))
                    # rotation +1

            # else
                # array is sorted

    # return rotations

# Function
def count_rotations_linear(nums):
    given = nums
    print(given)
    sort = False
    rotations = 0
    i = 0

    # test if list is empty
    if given == []:
        rotations = 0

    else:
        while not sort:
            if given[i] < given[i+1]:
                i = i + 1

            else:
                # move 1st to last position
                given.sort(key=given[0].__eq__)
                i = 0
                rotations = rotations +1

            if i == (len(given) - 1):
                sort = True

            else:
                continue

    return rotations

def count_rotations_binary(nums):
    given = nums

    rotations = 0
    array_sorted = False

    # get middle value of given
    og_mid_pos = (0 + len(given)) // 2
    og_mid = given[og_mid_pos]

    left, right = 0, (og_mid_pos - 1)

    while not array_sorted:

        test_mid_pos = (left+right) // 2
        test_num = given[test_mid_pos]

        if test_mid_pos == 0:
            array_sorted = True

        else:
            # check if number left and right of middle test are less than and greater than respectively
            if (given[test_mid_pos-1] < test_num) and (given[test_mid_pos+1] > test_num):
                # continue with this current iteration
                right = test_mid_pos

            else:
                # bigger number at end, use rotation
                given.sort(key=given[0].__eq__)
                rotations = rotations + 1
                right = og_mid_pos

        # print(given)

    return rotations


# TEST CASES
test0 = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}

# A list of size 8 rotated 5 times.
test1 = {
    'input': {
        'nums': [14, 19, 25, 29, 3, 5, 6, 7, 9, 11]
    },
    'output': 4
}

# list not rotated at all
test2 = {
    'input': {
        'nums': [1,2,3,4,7,8]
    },
    'output': 0
}

# list rotated once
test3 = {
    'input': {
        'nums': [50, 2, 6, 7, 9, 11, 12]
    },
    'output': 1
}

# A list that was rotated n-1 times, where n is the size of the list.
test4 = {
    'input': {
        'nums': [5, 6, 7, 9, 11, 14, 19, 25, 29, 3]
    },
    'output': 9
}

# A list that was rotated n times, where n is the size of the list
test5 = {
    'input': {
        'nums': [1,2,3,4,7,8]
    },
    'output': 0
}

# An empty list.
test6 = {
    'input': {
        'nums': []
    },
    'output': 0
}

# A list containing just one element.
test7 = {
    'input': {
        'nums': [4]
    },
    'output': 0
}

tests =[test0, test1, test2, test3, test4, test5, test6, test7]

### full tests ###

# nums0 = test1['input']['nums']
# output0 = test1['output']
# result0 = count_rotations_linear(nums0)

# print(result0, result0 == output0)

from jovian.pythondsa import evaluate_test_case


for i in range(0, len(tests)):
    evaluate_test_case(count_rotations_linear, tests[i])

# evaluation tests
#     nums = tests[i]['input']['nums']
#     output = tests[i]['output']
#     result = count_rotations_linear(nums)
#     print(result, result == output)
from random import randint
from time import time


def binary_search(x, ordered_list, start, end):
    if start > end:
        return False
    central_pos = (start + end) // 2
    central_element = ordered_list[central_pos]
    if x == central_element:
        return True
    if x < central_element:
        return binary_search(x, ordered_list, start, central_pos - 1)
    return binary_search(x, ordered_list, central_pos + 1, end)

def intersection_n2(list1, list2):
    count = 0
    for element in list1:
        if element in list2:
            count += 1
    return count

def intersection_nlogn(list1, list2):
    count = 0
    list2.sort()
    for element in list1:
        if binary_search(element, list2, 0, len(list2) - 1):
            count += 1
    return count

def intersection_n(list1, list2):
    count = 0
    element_set = set()
    for element in list1:
        element_set.add(element)
    for candidate in list2:
        if candidate in element_set:
            count += 1
    return count

def create_list(size, max_value):
    tempset = set()
    while len(tempset) < size:
        tempset.add(randint(1, max_value))
    return list(tempset)
       

def clock(method, arguments):
    start = time()
    result = method(*arguments)
    duration = time() - start
    print("Result = %d --- elapsed: %.6f seconds (%s)" %
          (result, duration, method.__name__))


while True:
    n = eval(input("\nSize: " ))
    if n == 0:
        break
    print("Generating lists..." )
    list1 = create_list(n, 100*n)
    list2 = create_list(n, 100*n)
    print("Running intersection algorithms...")
    clock(intersection_n2, (list1, list2))
    clock(intersection_nlogn, (list1, list2))
    clock(intersection_n, (list1, list2))
    print()

print("\nCiao!")
    













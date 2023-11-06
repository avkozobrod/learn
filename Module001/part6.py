'''
def binary_search(list_num , to_search):
    first_index = 0
    size = len(list_num)
    print(size)
    last_index = size - 1
    mid_index = (first_index + last_index) // 2
    # print(mid_index)
    mid_element = list_num[mid_index]
    # print(mid_element)

    is_found = True
    while is_found:
        if first_index == last_index:
            if mid_element != to_search:
                is_found = False
                return " Does not appear in the list"

        elif mid_element == to_search:
            return f"{mid_element} occurs in position {mid_index}"

        elif mid_element > to_search:
            new_position = mid_index - 1
            last_index = new_position
            mid_index = (first_index + last_index) // 2
            mid_element = list_num[mid_index]
            if mid_element == to_search:
                return f"{mid_element} occurs in position {mid_index}"

        elif mid_element < to_search:
            new_position = mid_index + 1
            first_index = new_position
            last_index = size - 1
            mid_index = (first_index + last_index) // 2
            mid_element = list_num[mid_index]
            if mid_element == to_search:
                return f"{mid_element} occurs in position {mid_index}"



list_container = [16 , 18 , 20 , 50 , 60 , 81 , 84 , 89]
print(binary_search(list_container , 81))
print(binary_search(list_container , 10))
'''

def binary_search2(list_num, first_index, last_index, to_search):
    if last_index >= first_index:

        mid_index = (first_index + last_index) // 2
        mid_element = list_num[mid_index]

        if mid_element == to_search:
            return f"{mid_element} occurs in position {mid_index}"

        elif mid_element > to_search:
            new_position = mid_index - 1
            # new last index is the new position
            return binary_search2(list_num, first_index, new_position, to_search)

        elif mid_element < to_search:
            new_position = mid_index + 1
            # new first index is the new position
            return binary_search2(list_num, new_position, last_index, to_search)

    else:
        return " Does not appear in the list"


list_container = [1, 9, 11, 21, 34, 54, 67, 90]
search = 34
first = 0
last = len(list_container) - 1

print(binary_search2(list_container, first, last, search))


# Creating a bubble sort function
def bubble_sort(list1):
    # Outer loop for traverse the entire list
    for i in range(0, len(list1) - 1):
        for j in range(len(list1) - 1):
            if (list1[j] > list1[j + 1]):
                temp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = temp
    return list1


list1 = [5, 3, 8, 6, 7, 2]
print("The unsorted list is: ", list1)
# Calling the bubble sort function
print("The sorted list is: ", bubble_sort(list1))

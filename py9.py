def merge_list(list1, list2):
    result_list = []

    for num in list1:
        if num % 2 != 0:
            result_list.append(num)

    for num in list2:
        if num % 2 == 0:
            result_list.append(num)

    return result_list


list1 = [10,20,25,36,54,11,63,80,99]
list2 = [40,60,80,55,47,49,97,99,96]

print("new list: ", merge_list(list1,list2))
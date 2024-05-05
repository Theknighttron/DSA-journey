def recursiveBinarySearch(list, target):
    # check if the list is empty
    if len(list) == 0:
        return False
    else:
        # find the midpoint
        midpoint = len(list) // 2

        # check if the midpoint is the target
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursiveBinarySearch(list[midpoint + 1:], target)
            else:
                return recursiveBinarySearch(list[:midpoint], target)


def verify(result):
    print("Target Found: ", result)


list = [1,2,3,4,5,6,7,8,9]

output = recursiveBinarySearch(list, 12)
verify(output)

output = recursiveBinarySearch(list, 6)
verify(output)


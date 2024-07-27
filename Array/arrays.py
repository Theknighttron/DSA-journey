new_list = [1, 2, 3, 4, 5]

# Accessing the element in the array
result = new_list[0]
print(result)


# Searching element in the array
if n in new_list:
    print(True)

    # Another way for searching

for n in new_list:
    if n == 1:
        print(True)

        break


# Inserting element in the array
new_list[0] = 9 # True inserting
# Time complexity is O(n) since we have to shift each element from the current index to the last index


new_list.append(6) # Appending the element to the end of the list
# Time complexity is O(1) since we are adding the element to the end of the list

new_list.extends((7, 8, 10]) # Adding a list to an existing array
#  Time complexity is O(k) where k is the number of element that we are adding to the array


# Deleting element from the array
new_list.remove(2) # remove the item from the certain index eg:2
new_list.pop(2) # remove the item from the certain index eg:2

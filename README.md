# ALGORITHMS AND DATA STRUCTURE

# ALGORITHMS
-- Algorithmic Thinking > Is an approach to problem solving that involves breaking down the problem to clearly defined input and output with along with
    the distinct set of steps that solves a problem.

### Steps to define and implement algorithms
-- The steps in the algorithm need to be in specific order.
-- The steps need to be distinct.
-- The algorithm should produce a result.
-- The algorithm should complete in a finite amount of time.

## SEARCHING ALGORITHMS

### LINEAR SEARCH
-- Time complexity of linear search is O(n)/linear because the problem is reduced by a half in each iteration.
-- Space complexity of linear search is O(1)/constant.

### BINARY SEARCH
-- Time complexity of binary search is O(log n)/logarithmic because the problem is reduced by a half in each iteration.
-- Space complexity of binary search is O(1)/constant.

### RECURSIVE BINARY SEARCH
-- Recursive function >  refers to the function that calls it's self.

Note:
"When using recursive function firstly you have to define the base case to avoid infinity looping"


-- Recusive Depth > refers to the number of times recursive function call's itself.
-- Space complexity of recursive binary search is O(log n)/logarithmic since every time when we call the function body
    We create a new sublist from the original list.




# DATA STRUCTURE
-- is a way of storing data or data storage format.
It is the collection of values and the format they are stored in, the relations ship between
the values in the collection as well as the operations applied on the data stored in the structure.


(Arrays) > is a fundamental data structure that can be used to represent a collection of values.
eg:
    array[a, b, c]
    -- each value in referenced using index or key from 0

homogeneous array > refers to array that only support one type data type within a single array. eg in java, swift
heterogeneous array > refers to array that support mutiple data type within a single array. eg in python

-- An array is a contiguos data structure

### Operations of data structures
-- Access and read values
-- Search for an arbitrary values
-- Insert values at any point into the structure
-- Delete values in the structure

LinkedList
is a linear data structure where each element in the list is contained in a separate object called Node

Head Node - this  Referes to the first node element / begging of the list
Tail Node - this Referes to the last node element / end of the list

Node - is a (Self Referencial Object) meaning A link to another node


LinkedList Forms
1. Singly Linked List
Each element stores a reference to the next node is the list

2. Doubly Linked List
Each element stores a reference to the both the node before and after


List traversal - Moving from one node to the next node

Inserting data to the list
1. Prepend - inserting data to the head
2. Append - inserting data to the tail
3. True insert - is where you can insert data at any point in the list

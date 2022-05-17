# Show Me the Data Structures Project

##  Problem 1: LRU
We've implemented the LRU cache using a double sided linked list which references to both head and tail.
All operations (insert, update, remove) have a worst case runtime complexity of O(1) since we hold references to both ends of the linked list and the swap during update also takes O(1) time.
The space complexity is O(n) since we keep as many elements in the linked list as there are values in the input.

##  Problem 2: Recursion
We've implemented the solution as a basic recursive walk through a directed asyclic graph (the directory hierarchy).
Since each node is only checked once, our algorithm has a runtime complexity of O(n).
The space complexity is O(m), where m is the number of files and directories, since we collect and return all the search results.

## Problem 3: Huffman Coding
Our solution is implemented using a frequency table, a minimum frequency heap, a binary tree structure, and a word encoding dictionary
The runtime complexity of building the frequency table is O(n^2) since we've n element and each insertion has a worst case runtime of O(n)
The worst case runtime complexity of building the min heap is O(n)
The worst case runtime complexity of building the Huffman tree is O(n)
The worst case runtime complexity of building the dictionary is O(n^2)
The worst case runtime complexity of building the output binary string is O(n^2)
In summary, the total worst case runtime complexity is O(n^2)
The overall space complexity is O(n) since each step i has a space complexity of O(n_i)

## Problem 4: Active Directory
Our solution is implemented as a recursive tree search over the groups,subgroups, and their respective users.
The worst case runtime complexity is O(n), where n is the number of total users across all groups
The overall space complexity is O(m) ,where m is the total number of groups and users 

## Problem 5: Blockchain
Our solution is implemented using a double sided linked list which holds references to both the tail and head nodes.
Insertion into our data-structure is an O(1) runtime operation.
The space complexity is O(n) since we keep as many blocks in the list as provided via input.

## Problem 6: Union and Intersection
Our solution utilized a uni-directional linked list (i.e the code provided by Udacity).
The union operation takes O(n^2) time due to each insertaion taking O(n) time.
The intersection operation takes O(n^3) time due to each membership check taking O(n) time (for n elements) and each insertion into the output list taking O(n) time.
The space complexity is O(n), where n is the total number of elements in the input lists, since at the worst case we concatenate and return both provided lists.


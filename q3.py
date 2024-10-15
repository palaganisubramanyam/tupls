'''
 Write a program to get the tuple elements in a single line separated by spaces and print the number of elements in the given tuple.
Sample Input:
10 20 30
Sample Output:
3
'''

def count_tuple_elements():
    elements = input("Enter the tuple elements separated by spaces: ").split()
    my_tuple = tuple(elements)
    print(len(my_tuple))
count_tuple_elements()

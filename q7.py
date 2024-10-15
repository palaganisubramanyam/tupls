'''
 Write a program to get the tuple values in a single line separated by space and count the nuber of times the given x value is present in the given tuple.
Sample Input:
1 2 3 1 2 3 4 1 2 1
1
Sample Output:
4
'''

def count_value_in_tuple():
    elements = input("Enter the tuple values separated by spaces: ").split()
    my_tuple = tuple(map(int, elements))
    x = int(input("Enter the value to count: "))
    count = my_tuple.count(x)
    print(count)
count_value_in_tuple()

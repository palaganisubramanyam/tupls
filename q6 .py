'''
Write a program to get n number of values from user in separate line and print the minimum value of the given tuple.
Sample Input:
3
20
30
10
Sample Output:
10
'''

def min_of_tuple_elements():
    n = int(input("Enter the number of elements: "))
    my_tuple = ()
    for _ in range(n):
        value = int(input("Enter a value: "))
        my_tuple += (value,)  # Add the value to the tuple
    min_value = min(my_tuple)
    print(min_value)
min_of_tuple_elements()

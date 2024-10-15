'''
 Write a program to get n number of tuple elements from the user in separate line and print the maximum value of the given values.
Sample Input:
3
20
10
30
Sample Output:
30
'''

def max_of_tuple_elements():
    n = int(input("Enter the number of elements: "))
    my_tuple = ()
    for _ in range(n):
        value = int(input("Enter a value: "))
        my_tuple += (value,)  # Add the value to the tuple
    max_value = max(my_tuple)
    print(max_value)
max_of_tuple_elements()

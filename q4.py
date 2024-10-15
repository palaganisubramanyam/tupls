'''
Write a program to get n number of tuple elements from the user in separate lines and print the sum of their values using predefined method.
Sample Input:
3
10
20
30
Sample Output:
60
'''


def sum_of_tuple_elements():
    n = int(input("Enter the number of elements: "))
    my_tuple = ()
    for _ in range(n):
        value = int(input("Enter a value: "))
        my_tuple += (value,)  # Add the value to the tuple
    total_sum = sum(my_tuple)
    print(total_sum)
sum_of_tuple_elements()

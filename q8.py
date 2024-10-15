'''
 Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
Sample Input:
10 20 30
Sample Output:
60
'''

def sum_of_tuple_elements():
    elements = input("Enter the tuple elements separated by spaces: ").split()
    my_tuple = tuple(map(int, elements))
    total_sum = 0
    for value in my_tuple:
        total_sum += value
    print(total_sum)
sum_of_tuple_elements()

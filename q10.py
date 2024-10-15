'''
 Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
Sample Input:
1 2 3 4 1 5 1
1
Sample Output:
6
'''


def count_and_factorial():
    elements = input("Enter the tuple elements separated by spaces: ").split()
    my_tuple = tuple(map(int, elements))
    x = int(input("Enter the number to count: "))
    count = my_tuple.count(x)
    factorial = 1
    for i in range(1, count + 1):
        factorial *= i
    print(factorial)
count_and_factorial()

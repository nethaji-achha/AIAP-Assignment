from asyncio import print_call_graph
#wriete a python function to calculate the sum of squares of a numbers in list

def sum_of_squares(numbers):
    return sum(x ** 2 for x in numbers)
    
print(sum_of_squares([1,2,3,4,5]))
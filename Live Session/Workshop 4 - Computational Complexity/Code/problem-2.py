'''
Create a function that takes in a list of numbers,
Calculate the sum of the numbers without using any built in methods
'''

def get_sum(numbers: list):
    output = 0

    for number in numbers:
        output += number

    return output

'''
Create a function that takes in a list of numbers,
you will need to return another list that contains only the even numbers 
that are preseent in the original list.
'''

def get_even_numbers(numbers: list):
    output = []

    for number in numbers:
        if number % 2 == 0:
            output.append(number)

    return output

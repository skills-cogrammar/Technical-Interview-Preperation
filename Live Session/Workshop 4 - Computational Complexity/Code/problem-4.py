'''
You are given a string 'sentence' an arrangement of characters 'substring'
You need to create a function that counts the number of times that `substring` occurs in `sentence`
'''

def get_substring_count(sentence, substring):
    counter = 0
    substring_length = len(substring)    

    for i in range(len(sentence)):
        start_index = i 
        end_index = i + substring_length

        if (end_index > len(sentence)):
            break

        current_substring = ''.join([sentence[char] for char in range(start_index, end_index)])
        
        if current_substring == substring:
            counter += 1


    return counter


# def get_substring_count(sentence, substring):
#     counter = 0
#     substring_length = len(substring)    

#     for i in range(len(sentence)):
#         start_index = i 
#         end_index = i + substring_length

#         if (end_index > len(sentence)):
#             break

#         current_substring = sentence[start_index:end_index]
#         print(current_substring)        
        
#         if current_substring == substring:
#             counter += 1


#     return counter
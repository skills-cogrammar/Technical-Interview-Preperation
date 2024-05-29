books = [
    "To Kill a Mockingbird", "1984", "The Great Gatsby", "The Catcher in the Rye",
    "Moby-Dick", "War and Peace", "Pride and Prejudice", "The Lord of the Rings",
    "The Hobbit", "Jane Eyre", "Wuthering Heights", "Brave New World",
    "The Odyssey", "Crime and Punishment", "The Brothers Karamazov",
    "Anna Karenina", "Madame Bovary", "The Adventures of Huckleberry Finn",
    "Alice's Adventures in Wonderland", "Don Quixote", "The Divine Comedy",
    "Ulysses", "One Hundred Years of Solitude", "The Iliad", "The Aeneid",
    "The Canterbury Tales", "Les Misérables", "Great Expectations", "Dracula",
    "Frankenstein", "The Count of Monte Cristo", "The Scarlet Letter",
    "Heart of Darkness", "Catch-22", "Lord of the Flies", "The Sound and the Fury",
    "Gone with the Wind", "Slaughterhouse-Five", "The Grapes of Wrath",
    "A Tale of Two Cities", "The Old Man and the Sea", "The Stranger",
    "The Sun Also Rises", "The Metamorphosis", "The Picture of Dorian Gray",
    "A Clockwork Orange", "The Bell Jar", "Beloved", "Invisible Man", "Fahrenheit 451",
    "Things Fall Apart", "No Longer at Ease", "Arrow of God", "A Man of the People",
    "Anthills of the Savannah", "When Rain Clouds Gather", "Maru", "A Question of Power",
    "Petals of Blood", "Weep Not, Child", "The River Between", "A Grain of Wheat",
    "Season of Migration to the North", "The Wedding of Zein", "Half of a Yellow Sun",
    "Purple Hibiscus", "Americanah", "So Long a Letter", "The Dark Child",
    "Chaka", "The Joys of Motherhood", "Nervous Conditions", "The Book of Not",
    "The Hairdresser of Harare", "The Beautiful Ones Are Not Yet Born", 
    "Waiting for the Barbarians", "Disgrace", "Cry, the Beloved Country",
    "Mine Boy", "Burger's Daughter", "July's People"
]



# Sorting the books alphabetically
def quicksort(arr):
    # Base case: an array of 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose the pivot element (using the middle element for simplicity)
    pivot = arr[len(arr) // 2]
    
    # Partition the array into three parts: less than, equal to, and greater than the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sort the left and right parts and concatenate the result
    return quicksort(left) + middle + quicksort(right)



def binary_search(book_list, target):
    # Initialize left and right pointers to the beginning and end of the list
    left, right = 0, len(book_list) - 1
    
    # Continue searching as long as left pointer does not exceed right pointer
    while left <= right:
        # Calculate the middle index of the current segment
        mid = (left + right) // 2
        
        # Check if the middle element is the target
        if book_list[mid] == target:
            return mid  # Target found at index mid
        
        # If target is greater than the middle element, search in the right half
        elif book_list[mid] < target:
            left = mid + 1  # Update left pointer to mid + 1
        
        # If target is less than the middle element, search in the left half
        else:
            right = mid - 1  # Update right pointer to mid - 1
    
    # If target is not found, return -1
    return -1

sorted_books = quicksort(books)
print("Sorted Books (Case-Insensitive):", sorted_books)
# Example usage of binary search
book_to_find = "Things Fall Apart"
index = binary_search(sorted_books, book_to_find)
if index != -1:
    print(f"Book '{book_to_find}' found at index {index}.")
else:
    print(f"Book '{book_to_find}' not found.")
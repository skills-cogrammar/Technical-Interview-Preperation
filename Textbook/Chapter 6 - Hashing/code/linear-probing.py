class HashSet:
    def __init__(self, size: int, load_factor: float) -> None:
        self.__size = size
        self.__filled_spaces = 0
        self.__load_factor = 1 if load_factor > 1 else load_factor
        self.__internal_array = [None] * size

    def add(self, value: str):
        self.__resize_array()

        index = hash
        self.__internal_array[index] = value    
        self.__filled_spaces += 1



    def __resize_array(self):
        filled_percentage = self.__filled_spaces / self.__size

        if filled_percentage < self.__load_factor:
            return 
        
        old_values = [value for value in self.__internal_array if value is not None]

        self.__size = self.__size * 2        
        self.__internal_array = [None] * self.__size

        for value in old_values:
            self.add(value)

    def contains(self, value: str):
        index = self.__hash(value)
        index = self.__linear_probing_search(index, value)
        return index > -1

    def __linear_probing_search(self, index, value, count=0):
        if self.__internal_array[index] == value:
            return index
        
        if count == self.__size:
            return -1
        
        if index == self.__size - 1:
            index = -1

        return self.__linear_probing_search(index + 1, value, count + 1)


    def __hash(self, value: str):
        ascii_values = sum([ord(char) for char in value])               
        return ascii_values % self.__size
    
    def __linear_probing_insertion(self, index):        
        if self.__internal_array[index] is None:
            return index 
            
        print("collison")

        if (index == self.__size - 1):
            index = -1

        return self.__linear_probing_insertion(index + 1)



    
    def print_internal_array(self):
        return print(self.__internal_array)
    



my_set = HashSet(4, 0.75)

for fruit in ["apple", "banana", "orange", "pear", "mango", "grape", "strawberry"]:
    my_set.add(fruit)

my_set.print_internal_array()

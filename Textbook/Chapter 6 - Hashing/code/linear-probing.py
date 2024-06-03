class HashSet:
    def __init__(self, size: int, loading_factor: float):
        self.__size = size
        self.__used_space = 0
        self.__loading_factor = 1 if loading_factor > 1 else loading_factor
        self.__internal_array = [None] * size

    def add(self, value: str):
        if self.contains(value):
           return
        
        self.__resize_array()
        
        index = self.__hash(value)
        index = self.__linear_probing_insertion(index)

        self.__internal_array[index] = value
        self.__used_space += 1        

    def __resize_array(self):
        filled_percentage = self.__used_space / self.__size                

        if filled_percentage < self.__loading_factor:
            return 
        
        self.__size = self.__size * 2

        old_values = [value for value in self.__internal_array if value is not None]
        self.__internal_array = [None] * self.__size

        for value in old_values:
            index = self.__hash(value)
            index = self.__linear_probing_insertion(index)
            self.__internal_array[index] = value        

    def contains(self, value):
        index = self.__hash(value)
        index = self.__linear_probing_search(index, value)
        return index > -1

    def remove(self, value):
        if not self.contains(value):
            return
        
        index = self.__hash(value)
        index = self.__linear_probing_search(index, value)
        
        self.__internal_array[index] = None    
        self.__used_space -= 1

    def __hash(self, value: str) -> int:
        ascii_values = [ord(char) for char in value]        
        return ascii_values[0] % self.__size
    
    def __linear_probing_search(self, index, value, count=0):
        if self.__internal_array[index] == value:
            return index
        
        if count == self.__size:
            return -1

        if index == self.__size - 1:
            index = 0

        return self.__linear_probing_search(index + 1, value, count + 1)

    
    def __linear_probing_insertion(self, index):        
        if self.__internal_array[index] is None:
            return index
        
        print("collison")
        if index == self.__size - 1:
            index = -1

        return self.__linear_probing_insertion(index + 1)
    
    def __str__(self) -> str:
        return str(self.__internal_array)
    

my_set = HashSet(4, 1)
my_set.add('coding')
my_set.add('is')
my_set.add('really')
my_set.add('fun')

print(my_set)
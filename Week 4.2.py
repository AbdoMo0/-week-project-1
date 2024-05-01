class MySet:
    def __init__(self):
        self.elements = []
    def add(self, x):
        i = 0
        while i < len(self.elements) and self.elements[i] < x:
            i += 1
        self.elements.insert(i, x)
    def remove(self, x):
        i = 0
        while i < len(self.elements) and self.elements[i] != x:
            i += 1
        if i < len(self.elements) and self.elements[i] == x:
            del self.elements[i]
    def contains(self, x):
        for element in self.elements:
            if element == x:
                return True
        return False

my_set = MySet()
my_set.add(3)
my_set.add(1)
my_set.add(2)
my_set.add(4)

print("Set elements:", my_set.elements)
my_set.remove(3)
print("Set elements after removing 3:", my_set.elements)
print("Does set contain 4?", my_set.contains(4))
print("Does set contain 3?", my_set.contains(3))

# you should use that the array is already sorted. please, rewrite a code without using ready operations as "remove" etc. you should go through the array using the loop

class MySet:
    def __init__(self):
        self.elements = []
    def add(self, x):
        if x not in self.elements:
            self.elements.append(x)
            self.elements.sort()
    def remove(self, x):
        if x in self.elements:
            self.elements.remove(x)
    def contains(self, x):
        return x in self.elements
my_set = MySet()
my_set.add(3)
my_set.add(1)
my_set.add(2)
my_set.add(4)

print("Set elements:", my_set.elements) 
my_set.remove(3)
print("Set elements:", my_set.elements)
print("Does set contain 5?", my_set.contains(4))  
print("Does set contain 3?", my_set.contains(3)) 

# Abdelrahman Mohamed 11/314a

# Correct! 3pts

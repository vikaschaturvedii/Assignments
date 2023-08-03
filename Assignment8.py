class A:
    def __init__(self, a, b, c):
        self.__a = a
        self._b = b
        self.c = c

    def display(self):
        print("Values in Class A:")
        print("a:", self.__a)
        print("b:", self._b)
        print("c:", self.c)


class B(A):
    def display(self):
        try:
            print("Values in Class B:")
            print("a:", self.__a)  # Accessing private member
        except AttributeError:
            print("Error: Private member 'a' cannot be accessed.")
        print("b:", self._b)
        print("c:", self.c)


# Example usage
obj_a = A(10, 20, 30)
obj_a.display()

print()

obj_b = B(40, 50, 60)
obj_b.display()

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def to_list(self):
        return self.items.copy()


def intersection_of_stacks(stack1, stack2):
    # Convert both stacks to lists to make the intersection easier
    list1 = stack1.to_list()
    list2 = stack2.to_list()

    # Find the intersection of both lists
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)

    # Return the intersection as a list
    return list(intersection)


# Ejemplo de uso
if __name__ == "__main__":
    # Pila de personajes del episodio V
    pila_ep5 = Stack()
    pila_ep5.push("Luke Skywalker")
    pila_ep5.push("Darth Vader")
    pila_ep5.push("Leia Organa")
    pila_ep5.push("Han Solo")
    pila_ep5.push("Chewbacca")
    pila_ep5.push("C-3PO")
    pila_ep5.push("R2-D2")
    pila_ep5.push("Yoda")

    # Pila de personajes del episodio VII
    pila_ep7 = Stack()
    pila_ep7.push("Luke Skywalker")
    pila_ep7.push("Leia Organa")
    pila_ep7.push("Han Solo")
    pila_ep7.push("Chewbacca")
    pila_ep7.push("C-3PO")
    pila_ep7.push("R2-D2")
    pila_ep7.push("Rey")
    pila_ep7.push("Finn")

    # Obtener la intersección de ambas pilas
    interseccion = intersection_of_stacks(pila_ep5, pila_ep7)
    print("Personajes que aparecen en ambos episodios:", interseccion)
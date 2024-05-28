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


def find_positions(stack, names):
    temp_stack = Stack()
    positions = {name: -1 for name in names}
    current_position = 1

    while not stack.is_empty():
        character, _ = stack.pop()
        if character in positions:
            positions[character] = current_position
        temp_stack.push((character, _))
        current_position += 1

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return positions


def more_than_5_movies(stack):
    result = []
    temp_stack = Stack()

    while not stack.is_empty():
        character, movies = stack.pop()
        if movies > 5:
            result.append((character, movies))
        temp_stack.push((character, movies))

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return result


def count_movies(stack, character_name):
    temp_stack = Stack()
    count = 0

    while not stack.is_empty():
        character, movies = stack.pop()
        if character == character_name:
            count = movies
        temp_stack.push((character, movies))

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return count


def characters_with_letters(stack, letters):
    result = []
    temp_stack = Stack()
    letters = set(letters)

    while not stack.is_empty():
        character, _ = stack.pop()
        if character[0] in letters:
            result.append(character)
        temp_stack.push((character, _))

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return result


# Ejemplo de uso
if __name__ == "__main__":
    pila_personajes = Stack()
    pila_personajes.push(("Iron Man", 10))
    pila_personajes.push(("Captain America", 9))
    pila_personajes.push(("Thor", 7))
    pila_personajes.push(("Black Widow", 8))
    pila_personajes.push(("Hulk", 5))
    pila_personajes.push(("Rocket Raccoon", 4))
    pila_personajes.push(("Groot", 4))

    # a. Posición de Rocket Raccoon y Groot
    positions = find_positions(pila_personajes, ["Rocket Raccoon", "Groot"])
    print("a. Posición de Rocket Raccoon:", positions["Rocket Raccoon"])
    print("a. Posición de Groot:", positions["Groot"])

    # b. Personajes que participaron en más de 5 películas
    print("b. Personajes que participaron en más de 5 películas:", more_than_5_movies(pila_personajes))

    # c. Películas en las que participó Black Widow
    print("c. Películas en las que participó Black Widow:", count_movies(pila_personajes, "Black Widow"))

    # d. Personajes cuyos nombres empiezan con C, D y G
    print("d. Personajes cuyos nombres empiezan con C, D y G:", characters_with_letters(pila_personajes, "CDG"))
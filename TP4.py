class Pokemon:
    def __init__(self, number, name, types, level):
        self.number = number
        self.name = name
        self.types = types
        self.level = level
    
    def __repr__(self):
        return f"Pokemon({self.number}, {self.name}, {self.types}, {self.level})"

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def insert(self, key, value):
        index = key % self.size
        self.table[index].append(value)
    
    def get_bucket(self, key):
        index = key % self.size
        return self.table[index]

# Función hash basada en tipo
def hash_type(type_str):
    return sum(ord(char) for char in type_str)

# Función hash basada en el último dígito del número
def hash_last_digit(number):
    return number % 10

# Función hash basada en el nivel dividido en 10 posiciones
def hash_level(level):
    return level // 10

# Crear las tablas hash
type_hash_table = HashTable(20)  # Suponemos 20 tipos diferentes
last_digit_hash_table = HashTable(10)  # Dígitos del 0 al 9
level_hash_table = HashTable(10)  # Niveles divididos en 10 posiciones

# Cargar Pokémons
def load_pokemon(pokemon):
    # Insertar en tabla por tipo
    for type_ in pokemon.types:
        type_key = hash_type(type_)
        type_hash_table.insert(type_key, pokemon)
    
    # Insertar en tabla por último dígito del número
    last_digit_key = hash_last_digit(pokemon.number)
    last_digit_hash_table.insert(last_digit_key, pokemon)
    
    # Insertar en tabla por nivel
    level_key = hash_level(pokemon.level)
    level_hash_table.insert(level_key, pokemon)

# Ejemplo de carga de Pokémon
pokemons = [
    Pokemon(123, "Pikachu", ["Eléctrico"], 25),
    Pokemon(145, "Zapdos", ["Eléctrico", "Volador"], 50),
    Pokemon(207, "Mareep", ["Eléctrico"], 18),
    Pokemon(349, "Magikarp", ["Agua"], 15)
]

for pokemon in pokemons:
    load_pokemon(pokemon)

# Mostrar Pokémons cuyos números terminan en 3, 7 y 9
def show_pokemons_by_last_digit(digits):
    for digit in digits:
        bucket = last_digit_hash_table.get_bucket(digit)
        for pokemon in bucket:
            print(pokemon)

print("Pokémons cuyos números terminan en 3, 7 y 9:")
show_pokemons_by_last_digit([3, 7, 9])

# Mostrar Pokémons cuyos niveles son múltiplos de 2, 5 y 10
def show_pokemons_by_level_multiples(multiples):
    for multiple in multiples:
        for i in range(0, level_hash_table.size):
            if i % multiple == 0:
                bucket = level_hash_table.table[i]
                for pokemon in bucket:
                    print(pokemon)

print("\nPokémons cuyos niveles son múltiplos de 2, 5 y 10:")
show_pokemons_by_level_multiples([2, 5, 10])

# Mostrar Pokémons de los tipos especificados
def show_pokemons_by_types(types):
    for type_ in types:
        key = hash_type(type_)
        bucket = type_hash_table.get_bucket(key)
        for pokemon in bucket:
            print(pokemon)

print("\nPokémons de tipo Acero, Fuego, Eléctrico, Hielo:")
show_pokemons_by_types(["Acero", "Fuego", "Eléctrico", "Hielo"])
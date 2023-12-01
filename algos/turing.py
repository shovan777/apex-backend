def find_len(animal_str: str):
    animal_names = animal_str.split("-")
    while len(animal_names[-1]) == 0:
        animal_names.pop()
    print(animal_names)


s = "Elephant"
find_len(s)


def get_word_count(file_contents):
    words = file_contents.split()
    return len(words)

def get_character_count(file_contents):
    character_counts = {}

    for char in file_contents:
        if char.lower() in character_counts:
            character_counts[char.lower()] += 1
        else:
            character_counts[char.lower()] = 1

    return character_counts

def sort_on(character_results_dict):
    return character_results_dict["num"]

def get_sorted_characters(character_counts):
    characters = []

    for character in character_counts:
        characters.append({
            "char": character,
            "num": character_counts[character]
        })

    characters.sort(reverse=True, key=sort_on)

    return characters

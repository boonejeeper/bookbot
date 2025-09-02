import sys
from stats import get_word_count, get_character_count, get_sorted_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1] # second argument is filepath
    book_contents = get_book_text(filepath)
    word_count = get_word_count(book_contents)
    character_count = get_character_count(book_contents)
    sorted = get_sorted_characters(character_count)

    print("============ BOOKBOT ============");
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------");
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character_details in sorted:
        if character_details["char"].isalpha():
            print(f"{character_details["char"]}: {character_details["num"]}")
    print("============= END ===============")
main()

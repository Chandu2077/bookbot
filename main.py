from stats import get_num_words, get_num_char, sort_list
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    # path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    num_char = get_num_char(text)
    sorted_list = sort_list(num_char)
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ==============")

main()



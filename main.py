import sys
from stats import count_words
from stats import char_count
from stats import sort_dict

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    #print(get_book_text("books/frankenstein.txt"))
    #count_words(get_book_text("books/frankenstein.txt"))
    count_words(get_book_text(book_path))
    #print(char_count(get_book_text("books/frankenstein.txt")))

    sorted_dict = sort_dict(char_count(get_book_text(book_path)))
    for d in sorted_dict:
        if d["char"].isalpha():
            print(f"{d['char']}: {d['num']}")

    
main()

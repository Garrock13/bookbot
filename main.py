import sys
from stats import get_num_words
from stats import get_num_chars

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    print_chars_report(convert_dict_to_list_with_only_alpha(num_chars))
    print(f"--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def convert_dict_to_list_with_only_alpha(dict):
    list = []
    for key in dict:
        if key.isalpha():
            list.append({"name": key, "num": dict[key]})
    list.sort(reverse=True, key=sort_by_num)
    return list

def sort_by_num(dict):
    return dict["num"]

def print_chars_report(list):
    for dict in list:
        name = dict["name"]
        num = dict["num"]
        print(f"{name}: {num}")

main()

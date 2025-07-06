from stats import count_num_words, count_chars, sorted_list_of_chars_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():

    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    # print(file_path)
    book_text = get_book_text(file_path)
    num_words = count_num_words(book_text)
    chars_dict = count_chars(book_text)
    sorted_list_of_chars_count_variable = sorted_list_of_chars_count(chars_dict)

    sorted_list_of_chars_count_variable_string = ""
    for item in sorted_list_of_chars_count_variable:
        sorted_list_of_chars_count_variable_string += f"{item["char"]}: {item["num"]}\n"


    print(f'''
============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{sorted_list_of_chars_count_variable_string.strip()}
============= END ===============''')


main()
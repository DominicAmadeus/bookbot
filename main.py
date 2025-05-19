from stats import count_words, count_characters, sort_dictionary
import sys

# take file path as string and return file file_contents
def get_book_text(path_to_file):
    # open the file as f and place contents into string
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

# prints the book report, only prints alphabet characters
def print_report (path_to_file, num_words, character_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    # character list is {char: 'c', count: integer}
    for item in character_list:
        char = item.get('char')
        if char.isalpha():
            # if the character is in the alphabet, print it and the number of occurences
            char_count = item.get('count')
            print(f"{char}: {char_count}")
    print("============= END ===============")

def main():
    # if a second argument is not supplied, direct how to use the program
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # get book path and use stats.py to get book details
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = count_words(book_text)
    character_list = sort_dictionary(count_characters(book_text))    

    # print report using book details
    print_report(file_path, num_words, character_list)


main()
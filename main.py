from stats import count_words, count_chars, pretty_report
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return str(contents)

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(get_book_text(filepath))} total words")
    print("--------- Character Count -------")
    #print(count_chars(get_book_text("books/frankenstein.txt")))

    pretty_list = pretty_report(count_chars(get_book_text(filepath)))
    for dict in pretty_list:
        if dict["char"].isalpha() == True:
            print(f"{dict["char"]}: {dict["num"]}")

    print("============= END ===============")

main()
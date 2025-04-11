from stats import get_char_count, sort_letter_count, get_word_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():

    if len(sys.argv) < 2 or len(sys.argv) >= 3:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        try:
            with open(filepath, 'r') as f:
                pass  # File exists, no action needed here
        except FileNotFoundError:
            raise ValueError(f"The provided path '{filepath}' is not a valid file.")
        except Exception as e:
            raise ValueError(f"An error occurred while opening the file: {e}")
    
    text = get_book_text(filepath)
    word_count = get_word_count(text)
    letter_count = sort_letter_count(get_char_count(text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter in letter_count:
        print(f"{letter['char']}: {letter['count']}")
    print("============= END ===============")

main()
import sys

from stats import chars_dict_to_sorted_list, get_char_count, get_word_count


def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        return f.read()


def print_report(
    path_to_file: str, word_count: int, sorted_chars: list[tuple[str, int]]
):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for c, count in sorted_chars:
        if c.isalpha():
            print(f"{c}: {count}")

    print("============= END ===============")


def main():
    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_word_count(text)
    num_chars = get_char_count(text)

    sorted_chars = chars_dict_to_sorted_list(num_chars)

    print_report(filepath, num_words, sorted_chars)


main()

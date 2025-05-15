import sys

from stats import count_characters_, count_words_, sort_character_count


def main() -> None:

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]

    r = get_book_text(file_path)
    wc = count_words_(r)
    cc = count_characters_(r)
    sc = sort_character_count(cc)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for c in sc:
        if c["char"].isalpha():
            print(f"{c['char']}: {c['num']}")

    print("============= END ===============")


def get_book_text(filepath: str) -> str:
    with open(filepath, "r") as f:
        file_contents = f.read()

    return file_contents


if __name__ == "__main__":
    main()

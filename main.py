path_to_file = "books/frankenstein.txt"


def sort_on(dict):
    return dict["num"]


def count_words(text):
    return len(text.split())


def count_letters(text):
    lowercase_text = text.lower()
    chars_list = []
    chars_set = set()
    for letter in lowercase_text:
        chars_set.add(letter)

    for letter in chars_set:
        letter_stats = {}
        if letter.isalpha():
            letter_stats = {
                "letter": letter,
                "num": lowercase_text.count(letter)
            }
            chars_list.append(letter_stats)

    return chars_list


def print_report(word_count, letters_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f'{word_count} words found in the document')
    print()
    for letter in letters_list:
        print(
            f'The "{letter["letter"]}" character was found {letter["num"]} times')

    print("--- End report ---")


def main():
    with open(path_to_file) as f:
        file_contents = f.read()
        letters_list = count_letters(file_contents)
        word_count = count_words(file_contents)
        letters_list.sort(reverse=True, key=sort_on)
        print_report(word_count, letters_list)


main()

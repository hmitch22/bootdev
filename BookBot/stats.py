def get_word_count(text: str) -> int:
    return len(text.split())


def sort_on(val: tuple[str, int]):
    return val[1]


def chars_dict_to_sorted_list(d: dict[str, int]) -> list[tuple[str, int]]:
    unsorted = []

    for k in d:
        unsorted.append((k, d[k]))

    return sorted(unsorted, reverse=True, key=sort_on)


def get_char_count(text: str) -> dict[str, int]:
    count_dict: dict[str, int] = {}

    for char in text:
        c = char.lower()

        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1

    return count_dict

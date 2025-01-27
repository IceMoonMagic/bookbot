from collections import Counter


def main(filepath: str) -> None:
    with open(filepath) as file:
        contents = file.read()
    report = gen_report(contents, filepath)
    print(report)


def count_words(string: str) -> int:
    return len(string.split())


def count_chars(string: str) -> Counter[str]:
    result = Counter()
    for char in string.lower():
        result[char] += 1
    return result


def gen_report(
    string: str, filepath: str, include_non_alpha: bool = False
) -> str:
    lines = [
        f"--- Begin `{filepath}` Report---",
        f"{count_words(string)} words found in the document.",
        "",
    ]

    char_counts = count_chars(string)
    for char, amount in char_counts.most_common():
        if char.isalpha() or include_non_alpha:
            lines.append(f"The character '{char}' was found {amount} times.")

    lines.append(f"--- End `{filepath}` Report ---")
    return "\n".join(lines)


if __name__ == "__main__":
    main("books/frankenstein.txt")

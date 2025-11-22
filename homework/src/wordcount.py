# obtain a list of files in the input directory
import os
import sys


def count_words(words):
    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1
    return counter


def preprocess_lines(all_lines):
    all_lines = [line.strip().lower() for line in all_lines]
    return all_lines


def read_all_lines(input_folder):
    all_lines = []
    input_file_list = os.listdir(input_folder)
    for filename in input_file_list:
        file_path = os.path.join(input_folder, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            all_lines.extend(lines)
    return all_lines


def split_into_words(all_lines):
    words = []
    for line in all_lines:
        words.extend(word.strip(",.!?") for word in line.split())
    return words


def write_word_counts(counter, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_path = os.path.join(output_folder, "wordcount.tsv")
    with open(output_path, "w", encoding="utf-8") as f:
        for key, value in counter.items():
            f.write(f"{key}\t{value}\n")


def main():
    """
    if len(sys.argv) != 3:
        print("Usage: python -m homework <input_folder> <output_folder>")
        sys.exit(1)
    """
    input_folder = "data/input"
    output_folder = "data/output"

    all_lines = read_all_lines(input_folder)
    all_lines = preprocess_lines(all_lines)
    words = split_into_words(all_lines)
    counter = count_words(words)
    write_word_counts(counter, output_folder)


if __name__ == "__main__":
    main()

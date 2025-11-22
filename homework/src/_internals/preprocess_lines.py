from homework.src._internals.count_words import count_words


def preprocess_lines(all_lines):
    all_lines = [line.strip().lower() for line in all_lines]
    return all_lines

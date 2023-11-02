import string

# TODO: Handle keywords sharing prefix
def get_regex_char_range(all_chars, excluded_chars):
    # Filter out excluded characters
    allowed_chars = sorted([c for c in all_chars if c not in excluded_chars])

    if not allowed_chars:
        return '[]'  # Empty set

    # Create the character ranges
    ranges = []
    start_char = allowed_chars[0]
    prev_char = start_char

    for c in allowed_chars[1:]:
        if ord(c) - ord(prev_char) > 1:
            if start_char == prev_char:
                ranges.append(start_char)
            else:
                ranges.append(f"{start_char}-{prev_char}")
            start_char = c
        prev_char = c

    # Add the last range or character
    if start_char == prev_char:
        ranges.append(start_char)
    else:
        ranges.append(f"{start_char}-{prev_char}")

    return f"[{''.join(ranges)}]"

def generate_regex_forbidden_keywords(keywords):
    # Create patterns for each keyword
    patterns = []
    for keyword in keywords:
        parts = []
        for i, char in enumerate(keyword):
            if i == 0:
                # parts.append(f"{char}[A-Za-z0-9_.]*")
                pass
            else:
                prev_chars = keyword[:i]
                parts.append(f"(\"{prev_chars}\" ({get_regex_char_range(set(string.ascii_letters + string.digits + '_' + '.'), {char})}[A-Za-z0-9_.]*)?)")
        parts.append(f"(\"{keyword}\" [A-Za-z0-9_.]+)")
        patterns.append('|'.join(parts))
    
    # Combine patterns with a separator
    full_pattern = '|'.join(patterns)

    # Combine with the base pattern
    first_chars = {keyword[0] for keyword in keywords}
    full_pattern = f"({get_regex_char_range(set(string.ascii_lowercase + string.digits + '_' + '.'), first_chars)}[A-Za-z0-9_.]*)|({full_pattern})"

    return full_pattern


# https://v2.ocaml.org/releases/4.07/htmlman/manual049.html
def read_ocaml_keywords():
    with open("ocaml_4_keywords.txt", "r") as f:
        text = f.read()
        # Split the text into lines
        lines = text.split("\n")

        # Initialize an empty set
        keywords = set()

        # Extract keywords from each line and add to the set
        for line in lines:
            if ',' in line:
                keyword = line.split(',')[0].strip()
                keywords.add(keyword)
        return keywords

# Too many keywords
# ocaml_keywords = read_ocaml_keywords()
# hazel_keywords = {"fun", "case", "test", "end", "if", "let", "in", "type", "true", "false"}

# For now, only pick a few keywords that begins with different first character
ocaml_keywords = { "match", "rec", "struct" }
hazel_keywords = {"fun", "case", "end", "let", "test", "in"}

all_keywords = hazel_keywords | ocaml_keywords
regex = generate_regex_forbidden_keywords(all_keywords)
print(regex)

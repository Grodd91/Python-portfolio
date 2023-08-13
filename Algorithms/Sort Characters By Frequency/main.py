def frequency_sort(s):
    char_count = collections.Counter(s)
    sorted_chars = sorted(char_count.keys(), key=lambda char: char_count[char], reverse=True)
    result = []
    for char in sorted_chars:
        result.append(char * char_count[char])
    return ''.join(result)

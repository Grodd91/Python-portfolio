def kmp_search(text, word):
    n, m = len(text), len(word)
    lps = compute_lps(word)
    i = j = 0
    while i < n:
        if word[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            print("Pattern found at index", i - j)
            j = lps[j - 1]
        elif i < n and word[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

def compute_lps(word):
    length = 0
    lps = [0] * len(word)
    i = 1
    while i < len(word):
        if word[i] == word[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

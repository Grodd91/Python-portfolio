def rabin_karp_search(text, word):
    n, m = len(text), len(word)
    word_hash = sum(ord(char) for char in word)
    text_hash = sum(ord(char) for char in text[:m])
    for i in range(n - m + 1):
        if text_hash == word_hash and text[i:i+m] == word:
            print("Pattern found at index", i)
        if i < n - m:
            text_hash = text_hash - ord(text[i]) + ord(text[i + m])

def find_anagrams(s, p):
    def is_anagram(counter1, counter2):
        return all(counter1[char] == counter2[char] for char in counter1)

    len_s, len_p = len(s), len(p)
    counter_p = collections.Counter(p)
    counter_s = collections.Counter(s[:len_p])
    result = []

    for i in range(len_s - len_p + 1):
        if is_anagram(counter_s, counter_p):
            result.append(i)
        if i + len_p < len_s:
            counter_s[s[i]] -= 1
            if counter_s[s[i]] == 0:
                del counter_s[s[i]]
            counter_s[s[i + len_p]] += 1

    return result

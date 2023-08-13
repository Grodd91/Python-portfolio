from collections import defaultdict, deque

def ladder_length(begin_word, end_word, word_list):
    if end_word not in word_list:
        return 0

    word_dict = defaultdict(list)
    for word in word_list:
        for i in range(len(word)):
            word_dict[word[:i] + '*' + word[i + 1:]].append(word)

    queue = deque([(begin_word, 1)])
    visited = set()

    while queue:
        current_word, level = queue.popleft()
        for i in range(len(current_word)):
            intermediate_word = current_word[:i] + '*' + current_word[i + 1:]
            for word in word_dict[intermediate_word]:
                if word == end_word:
                    return level + 1
                if word not in visited:
                    visited.add(word)
                    queue.append((word, level + 1))
            word_dict[intermediate_word] = []

    return 0

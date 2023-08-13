from collections import defaultdict, deque

def alien_order(words):
    graph = defaultdict(set)
    indegree = {char: 0 for word in words for char in word}

    for i in range(1, len(words)):
        prev_word, curr_word = words[i - 1], words[i]
        min_len = min(len(prev_word), len(curr_word))
        for j in range(min_len):
            if prev_word[j] != curr_word[j]:
                if curr_word[j] not in graph[prev_word[j]]:
                    graph[prev_word[j]].add(curr_word[j])
                    indegree[curr_word[j]] += 1
                break

    queue = deque([char for char in indegree if indegree[char] == 0])
    result = []

    while queue:
        char = queue.popleft()
        result.append(char)
        for next_char in graph[char]:
            indegree[next_char] -= 1
            if indegree[next_char] == 0:
                queue.append(next_char)

    return ''.join(result) if len(result) == len(indegree) else ''

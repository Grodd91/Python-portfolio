def can_finish(num_courses, prerequisites):
    graph = {i: [] for i in range(num_courses)}
    indegree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque([course for course in range(num_courses) if indegree[course] == 0])

    while queue:
        course = queue.popleft()
        for next_course in graph[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)

    return all(deg == 0 for deg in indegree)

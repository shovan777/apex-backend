def buddyStrings(s: str, goal: str) -> bool:
    count = len(s)
    # orig_s = s
    if len(s) != len(goal):
        return False
    # list_s = list(s)
    # list_goal = list(goal)
    # for i in range(count):
    #     print(list_s, list_goal)
    #     if list_s[i] == list_goal[i]:
    #         list_s.pop(i)
    #         list_goal.pop(i)
    stripped_s = ""
    stripped_goal = ""
    for letter in zip(s, goal):
        if letter[0] != letter[1]:
            stripped_s += letter[0]
            stripped_goal += letter[1]
    s = stripped_s
    orig_s = s
    goal = stripped_goal
    for i in range(count):
        tempi = s[i]
        for j in range(i + 1, count):
            # tempj = s[j]
            # if i == j:
            #     continue
            s = s[:i] + s[j] + s[i + 1 :]
            s = s[:j] + tempi + s[j + 1 :]
            # print(s)
            # s[j] = tempi
            # s[i] = s[j]
            if s == goal:
                return True
            s = orig_s
            # s[j] = s[i]
            # s[i] = tempi
    return False

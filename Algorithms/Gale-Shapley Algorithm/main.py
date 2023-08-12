def stable_marriage(men_preferences, women_preferences):
    n = len(men_preferences)
    engaged_men = [-1] * n
    engaged_women = [-1] * n
    next_proposal = [0] * n

    while None in engaged_men:
        proposer = next(i for i, m in enumerate(engaged_men) if m is None)
        woman = men_preferences[proposer][next_proposal[proposer]]
        next_proposal[proposer] += 1

        if engaged_women[woman] == -1:
            engaged_women[woman] = proposer
            engaged_men[proposer] = woman
        else:
            current_husband = engaged_women[woman]
            woman_preferences = women_preferences[woman]
            if woman_preferences.index(proposer) < woman_preferences.index(current_husband):
                engaged_men[current_husband] = None
                engaged_men[proposer] = woman
                engaged_women[woman] = proposer

    return list(enumerate(engaged_men))

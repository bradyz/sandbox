from random import randint
from itertools import permutations


def score(ordering, team_size):
    teams = [list() for _ in team_size]

    offset = 0
    for i, people in enumerate(team_size):
        for _ in range(people):
            teams[i].append(ordering[offset])
            offset += 1

    scores = [sum(team) for team in teams]

    return max(scores) - min(scores), teams


def team_sizes(teams_left, players_left):
    if teams_left < 0 or players_left <= 0:
        pass
    elif teams_left == 1:
        yield [players_left]
    else:
        for to_take in range(1, players_left):
            for team in team_sizes(teams_left-1, players_left-to_take):
                yield [to_take] + team


def solve(num_teams, abilities):
    result = float("inf")
    result_split = None

    for team_size in team_sizes(num_teams, len(abilities)):
        for ordering in permutations(abilities):
            tmp, tmp_split = score(ordering, team_size)

            if tmp < result:
                result = tmp
                result_split = tmp_split

    return result, result_split


if __name__ == "__main__":
    num_teams = randint(1, 5)
    num_scores = randint(num_teams, 8)
    abilities = [randint(1, 10) for _ in range(num_scores)]

    print("Splitting %s into %d teams." % (str(abilities), num_teams))

    result, result_split = solve(num_teams, abilities)

    print("Fairness Score: %.0f." % result)
    print("\n".join(map(str, result_split)))

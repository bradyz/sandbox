for _ in range(int(input())):
    n, m, k = map(int, input().split())
    votes = {"ANJIE": 0, "SAM": 0}
    states = {"ANJIE": 0, "SAM": 0}
    num = {}
    for _ in range(n):
        state, vote = map(int, input().split())
        num[state] = vote
    for _ in range(m):
        state, vote = input().split()
        votes[vote] += num[int(state)]
        states[vote] += 1
    if votes["ANJIE"] >= k and votes["SAM"] >= k:
        if states["ANJIE"] > states["SAM"]:
            print("ANJIE")
        elif states["ANJIE"] < states["SAM"]:
            print("SAM")
        else:
            print("TIE")
    elif votes["ANJIE"] >= k:
        print("ANJIE")
    elif votes["SAM"] >= k:
        print("SAM")
    elif states["ANJIE"] > states["SAM"]:
        print("ANJIE")
    elif states["ANJIE"] < states["SAM"]:
        print("SAM")
    else:
        print("TIE")

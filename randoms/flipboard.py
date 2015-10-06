import json
import requests


def dfs(x=-1, y=-1):
    global adjacents, path, parent, end, letter, s
    for x1, y1 in adjacents[(x, y)]:
        if (x1, y1) in parent:
            continue
        parent[(x1, y1)] = (x, y)
        if (x, y) == (-1, -1):
            url = "https://challenge.flipboard.com/start"
        else:
            url = "https://challenge.flipboard.com/step?s=" + str(s) + \
                "&x=" + str(x1) + "&y="+str(y1)
        response = requests.get(url)
        if (x, y) == (-1, -1):
            s = response.url.split("=")[1][:-2]
        response = json.loads(response.text)
        letter[(x1, y1)] = response["letter"]
        if response['end']:
            end = (x1, y1)
            return True
        adjacents[(x1, y1)] = adjacents.get((x1, y1), set()) | \
            set([(a['x'], a['y']) for a in response['adjacent']])
        if dfs(x1, y1):
            return True
    return False


def path(cur):
    result = list()
    while cur != (-1, -1):
        result.append(letter[cur])
        cur = parent[cur]
    return "".join(reversed(result))

if __name__ == "__main__":
    for t in range(3):
        adjacents = dict()
        letter = dict()
        parent = dict()
        end = (-1, -1)
        s = None
        adjacents[(-1, -1)] = set([(0, 0)])
        print("Case: " + str(t+1))
        dfs()
        print("S: " + str(s))
        print("Path: " + str(path(end)))
        check = "https://challenge.flipboard.com/check?s=" + str(s) + \
            "&guess=" + str(path(end))
        success = json.loads(requests.get(check).text)["success"]
        print("Success: " + str(success) + "\n")

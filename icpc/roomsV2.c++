#include <iostream>
#include <cstring>

using namespace std;

int T;
int N, M;
int r[2002][2002];
int match[2002];
bool visited[2002];
 
bool dfs (int u) {
    // go through all the right nodes
    for (int v = N+1; v <= N+M; v++) {
        if (r[u][v] && !visited[v]) {
            visited[v] = true;
            // can we push back the flow
            if (match[v] < 0 || dfs(match[v])) {
                match[v] = u;
                return true;
            }
        }
    }
    return false;
}
 
int bpm () {
    memset(match, -1, sizeof(match));
    int result = 0;
    // go through all the left nodes
    for (int u = 1; u <= N; u++) {
        memset(visited, false, sizeof(visited));
        if (dfs(u))
            result++;
    }
    return result;
}

int main () {
    cin >> T;
    for (int t = 0; t < T; ++t) {
        cin >> N >> M;
        // clear the graph
        for (int i = 1; i <= N+M; ++i)
            for (int j = 1; j <= N+M; ++j)
                r[i][j] = 0;
        for (int u = 1; u <= N; ++u) {
            int k;
            cin >> k;
            for (int i = 0; i < k; ++i) {
                int v;
                cin >> v;
                v += N;
                r[u][v] = 1;
            }
        }
        cout << bpm() << endl;
    }
    return 0;
}

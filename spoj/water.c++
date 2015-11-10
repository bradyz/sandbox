#include <iostream>
#include <cstring>
#include <climits>
#include <utility>
#include <vector>
#include <queue>
#include <map>

#define pii pair<int, int>
#define pipii pair<int, pii>

using namespace std;

int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};

int T;
int N, M;
int result;
int board[101][101];
bool vis[101][101];

bool inBound (int x, int y) {
    return x > 0 && x < N-1 && y > 0 && y < M-1;
}

void bfs (int x, int y) {
    queue<pii> pqueue;
    vector<pii> toInc;
    int minGreater = INT_MAX;
    bool stop = false;
    memset(vis, false, 101*101);
    pqueue.push(pii(x, y));
    vis[x][y] = true;
    // cout << "start: " << x << " " << y << endl;
    while (pqueue.size() > 0 && !stop) {
        int xC = pqueue.front().first;
        int yC = pqueue.front().second;
        pqueue.pop();
        toInc.push_back(pii(xC, yC));
        for (int i = 0; i < 4; ++i) {
            int xP = xC + dx[i];
            int yP = yC + dy[i];
            if (xP < 0 || xP >= N || yP < 0 || yP >= M || vis[xP][yP])
                continue;
            vis[xP][yP] = true;
            if (board[xP][yP] < board[x][y])
                stop = true;
            else if (inBound(xP, yP) && board[xP][yP] == board[x][y])
                pqueue.push(pii(xP, yP));
            else
                minGreater = min(minGreater, board[xP][yP]);
        }
        // cout << xC << " " << yC << " " << minGreater << endl;
    }
    if (stop)
        return;
    for (int i = 0; i < toInc.size(); ++i) {
        int xC = toInc[i].first;  
        int yC = toInc[i].second;  
        result += minGreater - board[xC][yC];
        board[xC][yC] = minGreater;
    }
}

void p () {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j)
            cout << board[i][j] << "\t";
        cout << endl;
    }
}

int main () {
    cin >> T;
    for (int t = 0; t < T; ++t) {
        cin >> N >> M;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                int height;
                cin >> height;
                board[i][j] = height;
            }
        }
        result = 0;
        // p();
        multimap<int, pair<int, int> > pqueue;
        for (int i = 1; i < N-1; ++i)
            for (int j = 1; j < M-1; ++j)
                pqueue.insert(pipii(board[i][j], pii(i, j)));
        while (pqueue.size() > 0) {
            int x = pqueue.begin()->second.first;
            int y = pqueue.begin()->second.second;
            pqueue.erase(pqueue.begin()); 
            bfs(x, y); 
        }
        // cout << endl;
        // p();
        cout << result << endl;
    }
    return 0;
}

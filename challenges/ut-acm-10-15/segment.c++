#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <unordered_map>

using namespace std;

struct Node {
    int id;
    string val;
    int pid;
    Node (int a=0, string b="0", int c=-1) : id(a), val(b), pid(c) {};
};

int t;
int n;
string val;
int par;

int main () {
    cin >> t;
    for (int ct = 0; ct < t; ++ct) {
        cin >> n;
        unordered_map<int, Node> nodes;
        unordered_map<int, vector<int> > graph;
        unordered_map<int, int> miss;
        nodes[-1] = Node(-1, ".", -1);
        for (int cn = 0; cn < n; ++cn) {
            cin >> val >> par;
            nodes[cn] = Node(cn, val, par);
            graph[par].push_back(cn);
            if (val == "?")
                miss[par] += 1;
        }
        queue<Node> ones;
        for (auto it: miss) {
            if (nodes[it.first].val != "?" && it.second == 1)
                ones.push(nodes[it.first]);
        }
        while (ones.size() > 0) {
            int missChild = -1;
            Node cur = ones.front();
            ones.pop();
            for (auto child: graph[cur.id]) {
                if (nodes[child].val == "?") 
                    missChild = nodes[child].id;
            }
            if (graph[cur.id].size() != 1) {
                int sum = 0;
                bool found = false;
                for (auto child: graph[cur.id]) {
                    if (nodes[child].val != "?") {
                        sum += stoi(nodes[child].val);
                        found = true;
                    }
                }
                if (found) {
                    if (miss.find(cur.pid) != miss.end()) {
                        miss[cur.pid] -= 1;
                        if (miss[cur.pid] == 1 && nodes[cur.pid].val != "?")
                            ones.push(nodes[cur.pid]);
                    }
                    miss.erase(cur.id);
                    nodes[missChild].val = to_string(stoi(cur.val) - sum);
                }
            }
            else if (miss.find(missChild) == miss.end()) {
                int sum = 0;
                for (auto it: graph[missChild])
                    sum += stoi(nodes[it].val);
                if (miss.find(cur.pid) != miss.end()) {
                    miss[cur.pid] -= 1;
                    if (miss[cur.pid] == 1 && nodes[cur.pid].val != "?")
                        ones.push(nodes[cur.pid]);
                }
                if (cur.val == "." || cur.val == "?")
                    nodes[missChild].val = to_string(sum);
                else 
                    nodes[missChild].val = to_string(stoi(cur.val) - sum);
                miss.erase(cur.id);
            }
        }
        if (miss.size() == 0) {
            for (int i = 0; i < n; ++i) {
                cout << nodes[i].val;
                if (i != n-1)
                    cout << " ";
            }
            cout << endl;
        }
        else
            cout << "IMPOSSIBLE" << endl;
        // for (auto i: nodes)
        //     cout << "id: " << i.first << " val: " << i.second.val << endl;
        // for (auto i: miss)
        //     cout << "id: " << i.first << " missing: " << miss[i.first] << endl;
        // cout << endl;
    }
}

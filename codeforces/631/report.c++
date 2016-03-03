#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n, m;
int a[200005];
vector<vector<int> > q;

int main () {
    cin >> n >> m;
    for (int i = 0; i < n; ++i)
        cin >> a[i];

    int final_range; 
    int final_query; 

    for (int i = 0; i < m; ++i) {
        vector<int> t;
        int x, y;
        cin >> x >> y;

        t.push_back(-y);
        t.push_back(i);
        t.push_back(x);
        
        final_range = y;
        final_query = x;

        q.push_back(t);
    }

    sort(q.begin(), q.end());

    int max_order = -1;

    for (int i = 0; i < m; ++i) {
        int range, order, query;
        range = -q[i][0];
        order = q[i][1];
        query = q[i][2];

        if (range < final_range)
            break;
        else if (order < max_order)
            continue;

        max_order = order;

        if (query == 1)
            sort(a, a+range);
        else
            sort(a, a+range, greater<int>());
    }
    
    if (final_query == 1)
        sort(a, a+final_range);
    else
        sort(a, a+final_range, greater<int>());

    for (int i = 0; i < n; ++i) {
        cout << a[i];
        if (i != n-1)
            cout << " ";
    }
    cout << endl;
    return 0;
}

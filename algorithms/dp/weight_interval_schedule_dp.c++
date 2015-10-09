#include <iostream>
#include <algorithm>

using namespace std;

struct Job {
    int start;
    int end;
    int weight;

    friend ostream& operator<< (ostream& os, Job& job) {
        os << "Start: " << job.start;
        os << " End: " << job.end; 
        os << " Weight: " << job.weight;
        return os;
    }
};

bool sortFunction (Job lhs, Job rhs) {
    return lhs.end < rhs.end;
}

int latestWithoutConflict (Job jobs[], int i) {
    for (int j = i-1; j >= 0; --j) {
        if (jobs[j].end <= jobs[i].start)
            return j;
    }
    return -1;
}

int maxProfit (Job jobs[], int n) {
    sort(jobs, jobs+n, sortFunction);

    int dp[n];

    for (int i = 0; i < n; ++i) {
        int withJobi = jobs[i].weight;
        
        int j = latestWithoutConflict(jobs, i);

        if (j >= 0) 
            withJobi += jobs[j].weight;
        
        dp[i] = max(withJobi, dp[i-1]);
    }

    return dp[n-1];
}

int main () {
    Job jobs[] = {{3, 10, 20}, {1, 2, 50}, {6, 19, 100}, {2, 100, 200}};
    int n = sizeof(jobs)/sizeof(jobs[0]);


    for (int i = 0; i < n; ++ i)
        cout << jobs[i] << endl;

    cout << maxProfit(jobs, n) << endl;

    return 0;
}

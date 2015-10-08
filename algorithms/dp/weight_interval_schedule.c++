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
    if (n == 1)
        return jobs[0].weight;
    
    int withLastJob = jobs[n-1].weight;
    int i = latestWithoutConflict(jobs, n-1);

    if (i >= 0) 
        withLastJob += jobs[i].weight;

    int withoutLastJob = maxProfit(jobs, n-1);

    return max(withLastJob, withoutLastJob);
}

int main () {
    Job jobs[] = {{3, 10, 20}, {1, 2, 50}, {6, 19, 100}, {2, 100, 200}};
    int n = sizeof(jobs)/sizeof(jobs[0]);

    sort(jobs, jobs+n, sortFunction);

    for (int i = 0; i < n; ++ i)
        cout << jobs[i] << endl;

    cout << maxProfit(jobs, n) << endl;

    return 0;
}

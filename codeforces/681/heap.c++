#include <iostream>
#include <cstdio>
#include <queue>
#include <vector>
#include <string>

using namespace std;

int n;
char buff[10];

int main () {
  scanf("%d", &n);
  priority_queue<int> pq;
  vector<string> r;
  for (int i = 0; i < n; ++i) {
    scanf("%s", &buff);
    string s = buff;
    if (s == "removeMin") {
      if (pq.size() == 0)
        r.push_back("insert 0");
      else
        pq.pop();
      r.push_back("removeMin");
    }
    else {
      int x;
      scanf("%d", &x);
      if (s == "insert") {
        pq.push(x);
        r.push_back("insert " + to_string(x));
      }   
      else {
        while (pq.size() > 0 && pq.top() < x) {
          pq.pop();
          r.push_back("removeMin");
        }
        if (pq.size() == 0 || pq.top() > x) {
          r.push_back("insert " + to_string(x));
          pq.push(x);
        }
        r.push_back("getMin " + to_string(x));
      }
    }
  }
  printf("%d\n", r.size());
  for (string s : r)
    printf("%s\n", s.c_str());
  return 0;
}

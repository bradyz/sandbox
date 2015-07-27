#include <iostream>
#include <algorithm>

using namespace std;

int v[1000];
int w[1000];
int x, y;

int knapSack(int a, int b){
   if(a == 0 || b == 0)
       return 0;
 
   if (w[b-1] > a)
       return knapSack(a, b-1);
   else 
       return max(v[b-1] + knapSack(a-w[b-1], b-1), knapSack(a, b-1));
}
 
int main(){
    cin >> x >> y;

    for(int i = 0; i < y; ++i)
        cin >> w[i] >> v[i];
    
    cout << knapSack(x, y) << endl;
}

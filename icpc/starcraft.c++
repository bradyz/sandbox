#include <iostream>

using namespace std;

int T;
int S, A, P, M, D, B, Z;

int main () {
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> S >> A >> P >> M >> D >> B >> Z;
        unsigned long long maxZealots = 0;
        unsigned long long maxN = 0;
        for (int N = 0; N < S; ++N) {
            unsigned long long minerals = 100;
            unsigned long long pylons = 1;
            unsigned long long drones, zealots = 0;
            for (int n = 0; n < N; ++n) {
                // step 1
                int posPylons = min(drones, minerals/P);
                minerals -= posPylons * P; 
                pylons += posPylons;
                // step 2
                minerals += (drones - posPylons) * M;
                // step 3;
                int posDrones = min(B * pylons - drones, minerals/D);
                drones += posDrones;
                minerals -= posDrones * D;
            }
            for (int n = N; n < S; ++n) {
                // step 1
                int posPylons = min(drones, minerals/P);
                minerals -= posPylons * P; 
                pylons += posPylons;
                // step 2
                minerals += (drones - posPylons) * M;
                // step 3
                int posZealots = min(B * pylons - (drones + zealots), minerals / Z);
                zealots += posZealots;
                minerals -= posZealots * Z;
            }
            if (zealots > maxZealots) {
                maxZealots = zealots;
                maxN = N;
                cout << N << " " << maxZealots << endl;
            }
        }
        cout << "Case " << t << ": " << maxN << endl;
    }
}

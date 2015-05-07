#include <iostream>

#include "my-vector.h"

int main() {
    myqueue<int> a;

    for(int i = 0; i < 10; ++i)
        a.push(i);

    for(int i = 0; i < 10; ++i) {
        cout << a.front() << endl;
        a.pop();
    }

    return 0;
}

#include <vector>

using namespace std;

template <typename T>
class myqueue: vector<T> {
    public:
        myqueue () : vector<T>() {}

        void pop() {
            vector<T>::erase(vector<T>::begin());
        }

        void push(const T& val) {
            vector<T>::push_back(val);
        }

        T& front() {
            return vector<T>::front();
        } 
};

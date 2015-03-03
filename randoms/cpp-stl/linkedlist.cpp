#include <stddef.h>
#include <iostream>

template <typename T>
class node {
    public: 
        T _val;
        node <T> *next;

        node (): _val(), next() {}

        node (T val): _val(val), next() {}

        T operator*() {
            return _val;
        }
};

template <typename T>
class linkedlist {
    private:
        node <T> beg;

    public:
        class iterator {
            private:
                node <T> *_v;

            public:
                iterator (node<T> *pos): _v(pos) {}

                node <T> &operator++() {
                    _v = _v->next;
                    return *_v;
                }

                bool operator==(const node <T> &other) const {
                    return _v == other;
                }

                node <T> operator*() {
                    return **_v;
                }
        };

    public:
        linkedlist (): beg() {}

        bool add(const node <T> &el) {
            for(iterator it = begin(); it != NULL; ++it) {
                if(*it->next == NULL) {
                    *it->next = el;
                    return true;
                }
            }
            return false;
        }

        node <T> *begin() {
            return &beg;
        }
};

int main() {
    linkedlist <int> mylist = linkedlist<int>();
    mylist.add(1);
    mylist.add(2);
    mylist.add(3);

    for(linkedlist<int>::iterator it = mylist.begin(); it != NULL; ++it) {
        std::cout << *it << std::endl;
    }
}

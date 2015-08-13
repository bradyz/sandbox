#include <iostream>
#include <algorithm>

using namespace std;

struct Node {
    int _value;
    Node* _left;
    Node* _right;

    Node (int value=0, Node* left=NULL, Node* right=NULL) :
        _value(value),
        _left(left),
        _right(right) 
    {}

    friend ostream& operator<< (ostream& os, const Node& rhs) {
        return os << rhs._value;
    }
};

unsigned int depth (Node* root) {
    if (root == NULL) 
        return 0;
    return max(depth(root->_left), depth(root->_right)) + 1;
}

void leftrightmax (Node* root, int cur, int& low, int& high) {
    if (root == NULL)
        return;
    low = min(low, cur);
    high = max(high, cur);
    // cout << *root << " " << low << " " << high << endl;
    leftrightmax(root->_left, cur-1, low, high);
    leftrightmax(root->_right, cur+1, low, high);
}

unsigned int width (Node* root) {
    int left, right = 0;
    leftrightmax(root, 0, left, right);
    return right - left;
}

unsigned int area (Node* root) {
    return (depth(root)-1) * width(root);
}

//   ----a--
//   |  / \|
//   | f   b
//   |    /|
//   |   c |  each edge is length 1
//   |  /  |
//   | d   |
//   |/    |
//   e------

int main () {
    Node a(1);
    Node b(2);
    Node c(3);
    Node d(4);
    Node e(5);
    Node f(6);

    a._right = &b;
    a._left = &f;
    b._left = &c;
    c._left = &d;
    d._left = &e;

    cout << area(&a) << endl;
}

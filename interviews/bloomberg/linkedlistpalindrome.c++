#include <iostream>
#include <vector>

using namespace std;

struct Node {
    int value;
    Node* next;
};

Node* middle (Node* head) {
    Node* tmp = head;
    int length = 0;

    while (tmp->next) {  
        tmp = tmp->next;
        ++length;
    }

    tmp = head;
    length /= 2;

    while (length >= 0) {
        --length;
        tmp = tmp->next;
    }

    return tmp;
}

void walk (Node* head) {
    while (head) {
        cout << head->value;
        head = head->next;
    }
    cout << endl;
}


Node* reverse (Node* head) {
    Node* cur = head;
    Node* prev = NULL;
    Node* tmp;

    while (cur) {
        tmp = cur->next;
        cur->next = prev;
        prev = cur;
        cur = tmp;
    }

    return prev;
}

bool isPalindrome (Node* head) {
    Node* mid = middle(head);
    Node* tmp = reverse(middle(head));
    bool result = true;

    while (head && tmp) {
        if(tmp->value != head->value)
            return false;
        tmp = tmp->next;
        head = head->next;
    }

    return true;
}

bool isPalindromeV2 (Node* head) {
    vector<Node *> c;
    while (head) {
        c.push_back(head);
        head = head->next;
    }
    for(int i = 0; i < c.size() / 2; ++i) {
        if (c[i]->value != c[c.size()-i-1]->value) 
            return false;
    }
    return true;
}

int main () {
    Node a;
    Node b;
    Node c;
    Node d;
    Node e;

    a.value = 1;
    a.next = &b;

    b.value = 2;
    b.next = &c;

    c.value = 3;
    c.next = &d;

    d.value = 2;
    d.next = &e;

    e.value = 1;
    e.next = NULL;

    cout << isPalindromeV2(&a) << endl;
    cout << isPalindrome(&a) << endl;

    return 0;
}

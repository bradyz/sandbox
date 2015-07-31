#include <iostream>

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

void walk (Node* head) {
    while (head) {
        cout << head->value << endl;
        head = head->next;
    }
}

bool isPalindrome (Node* head) {
    Node* mid = middle(head);
    bool result = true;

    while (mid->next) {
        if(mid->value != head->value)
            cout << mid->value << " " << head->value << endl;
            return false;
        mid = mid->next;
        head = head->next;
    }

    return true;
}

int main () {
    Node a;
    Node b;
    Node c;
    Node d;

    a.value = 1;
    a.next = &b;

    b.value = 2;
    b.next = &c;

    c.value = 2;
    c.next = &d;

    d.value = 1;
    d.next = NULL;

    cout << isPalindrome(&a);

    return 0;
}

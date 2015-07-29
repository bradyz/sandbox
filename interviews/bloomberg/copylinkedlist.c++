#include <iostream>
#include <unordered_map>
#include <utility>
#include <vector>
#include <string>

using namespace std;

struct Node {
    string name;
    Node* value;
    Node* next;
};

void printLinkedList (Node* head) {
    while (head) {
        cout << "Name: " << head->name << " Value: ";
        cout << ((head->value != NULL) ? head->value->name : "NULL");
        cout << " Next: ";
        cout << ((head->next != NULL) ? head->next->name : "END") << endl;
        head = head->next;
    }
}

void copyLinkedList(Node* oldHead) {
    Node* head = oldHead;
    vector<Node*> c;
    unordered_map<Node*, pair<int, Node*> > d;
    int num = 0;

    while (head) {
        d[head] = pair<int, Node*>(num, head->value);
        Node* tmp = new Node();
        tmp->name = head->name;

        if (num > 0)
            c[num-1]->next = tmp;

        c.push_back(tmp);

        head = head->next;
        ++num;
    }
    
    head = oldHead;

    for (int i=0; i < num; ++i) {
        c[i]->value = d[head].second; 
        head = head->next;
    }

    cout << endl;

    printLinkedList(c[0]);

    head = c[0];
    Node* prev = NULL;

    while (head) {
        if (prev != NULL)
            free(prev);
        prev = head;
        head = head->next;
    }
}

int main() {
    Node a;
    Node b;
    Node c;
    Node d;

    a.name = "a";
    a.value = &d;
    a.next = &b;

    b.name = "b";
    b.value = NULL;
    b.next = &c;

    c.name = "c";
    c.value = &a;
    c.next = &d;

    d.name = "d";
    d.value = &c;
    d.next = NULL;

    printLinkedList(&a);
    copyLinkedList(&a);

    return 0;
}

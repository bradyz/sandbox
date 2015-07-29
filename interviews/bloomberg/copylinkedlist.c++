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

void copyLinkedList(Node* oldHead) {
    Node* head = oldHead;
    vector<Node> c;
    unordered_map<Node*, pair<int, Node*> > d;
    int num = 0;

    while (head) {
        d[head] = pair<int, Node*>(num, head->value);
        c.push_back(Node());

        if (num > 1)
            c[num-1].next = &c[num];

        head = head->next;
        ++num;
    }
    
    for (int i=0, Node* head=oldHead; i<num, head!=NULL; ++i, head=head->next) {
        c[i].value = 
    }
}

void printLinkedList (Node* head) {
    while (head) {
        cout << "Name: " << head->name << " Value: ";
        cout << ((head->value != NULL) ? head->value->name : "NULL");
        cout << " Next: ";
        cout << ((head->next != NULL) ? head->next->name : "END") << endl;
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

    return 0;
}

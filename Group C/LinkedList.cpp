#include <iostream>

using namespace std;

struct Node {
    int n;
    struct Node * next;
};

void printlist(struct Node * ptr) {
    while (ptr != NULL) {
        cout << ptr -> n << " ";
        ptr = ptr -> next;
    }
    cout << "\n";
}


int main() {
    Node * head = NULL;
    Node * second = NULL;
    Node * third = NULL;
    Node * fourth = NULL;
    Node * fifth = NULL;
    Node * sixth = NULL;

    head = new Node();
    second = new Node();
    third = new Node();
    fourth = new Node();
    fifth= new Node();
    sixth = new Node();

    head -> n = 1;
    head -> next = second;
    second -> n = 2;
    second -> next = third;
    third -> n = 3;
    third -> next = fourth;
    fourth -> n = 4;
    fourth -> next = fifth;
    fifth -> n = 5;
    fifth -> next = sixth;
    sixth -> n = 6;
    sixth -> next = NULL;
    cout<<"Origional node \n";
    printlist(head);


    // Enter node in the beginning.
    Node * newNode1 = new Node();
    newNode1 -> n = 7;
    newNode1 -> next = head;
    head = newNode1;

    // Enter node at the end.
    Node * newNode2 = new Node();
    newNode2 -> n = 8;
    struct Node * temp = head;
    while (temp -> next != NULL) {
        temp = temp -> next;
    }
    temp -> next = newNode2;
    newNode2 -> next = NULL;
    
    // Enter node in between.
    int pos = 2;
    Node * newNode3 = new Node();
    newNode3 -> n = 9;
    struct Node * ptr = head;
    for (int i = 0; i < pos; i++) {
        if (ptr != NULL) {
            ptr = ptr -> next;
        }
    }
    newNode3 -> next = ptr -> next;
    ptr -> next = newNode3;
    cout<<"After Adding Node \n";
    printlist(head);

    // Delete a node from beginning.
    head = head -> next;

    // Delete a node from the end.
    temp = head;
    while (temp -> next -> next != NULL) {
        temp = temp -> next;
    }
    temp -> next = NULL;

    // Delete a node from middle.
    int pos1 = 1;
    temp = head;
    for (int i = 0; i < pos1; i++) {
        if (temp != NULL) {
            temp = temp -> next;
        }
    }
    temp -> next = temp -> next -> next; 
    cout<<"After Deleteing Pointer Node\n";

    printlist(head);

    return 0;
}
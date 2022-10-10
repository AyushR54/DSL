#include <iostream>

using namespace std;

struct Node {
    string PRN;
    string Name;
    struct Node * next;
};

void Delete(Node * president) {
    string value = "Viren";
    Node * newNode = new Node();
    newNode -> Name = value;
    struct Node * temp = president;
    while (temp -> next != NULL) {
        if (temp -> next == value) {
            temp -> next = temp -> next -> next;
            break;
        }
        temp = temp -> next;
    }
}

void display(struct Node * ptr) {
    while (ptr != NULL) {
        cout << ptr -> PRN << ": " << ptr -> Name << endl;
        ptr = ptr -> next;
    }
}

int main() {
    Node * president = NULL;
    Node * viceprecident = NULL;
    Node * member = NULL;

    president = new Node();
    viceprecident = new Node();
    member = new Node();

    president -> PRN = "F21113028";
    president -> Name = "Ayush";
    president -> next = viceprecident;

    viceprecident -> PRN = "F21113026";
    viceprecident -> Name = "Viren";
    viceprecident -> next = member;

    member -> PRN = "F21113000";
    member -> Name = "XYZ";
    member -> next = NULL;

    Delete(president);
    display(president);

    return 0;
}
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
    Node * second = NULL;
    Node * secretary = NULL;

    president = new Node();
    second = new Node();
    secretary = new Node();

    president -> PRN = "F21113028";
    president -> Name = "Ayush";
    president -> next = second;

    second -> PRN = "F21113026";
    second -> Name = "Viren";
    second -> next = secretary;

    secretary -> PRN = "F21113000";
    secretary -> Name = "XYZ";
    secretary -> next = NULL;

    Delete(president);
    display(president);

    return 0;
}
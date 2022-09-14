#include <iostream>

using namespace std;

struct Node {
    string PRN;
    string Name;
    struct Node * next;
};

void insert(Node * first, string prn, string name) {
    struct Node * ptr = first;
    Node * newNode = new Node();
    newNode -> PRN = prn;
    newNode -> Name = name;

    while (ptr -> next -> next != NULL) {
        ptr = ptr -> next;
    }
    newNode-> next = ptr -> next;
    ptr -> next = newNode;
}

void Delete(Node * president, string value) {
    Node * newNode = new Node();
    newNode -> Name = value;
    struct Node * temp = president;
    while (temp -> next != NULL) {
        if (temp -> next == newNode) {
            temp -> next = temp -> next -> next;
            break;
        }
        temp = temp -> next;
    }
}

int totalMembers(Node * president) {
    int count = 0;
    struct Node * ptr = president;
    while (ptr != NULL) {
        count++;
        ptr = ptr -> next;
    }
    return count;
}

void display(struct Node * ptr) {
    while (ptr != NULL) {
        cout << ptr -> PRN << ": " << ptr -> Name << endl;
        ptr = ptr -> next;
    }
}


int main() {
    Node * president = NULL;
    Node * secretary = NULL;

    president = new Node();
    secretary = new Node();

    president -> PRN = "F21113028";
    president -> Name = "Ayush";
    president -> next = secretary;

    secretary -> PRN = "F21113000";
    secretary -> Name = "XYZ";
    secretary -> next = NULL;
    
    cout << "CHOOSE FROM THE GIVEN OPTIONS\n";
    while (true) {
        string prn, name;
        cout << "\n";
        cout << "1. Add a member." << endl;
        cout << "2. Delete a member." << endl;
        cout << "3. Compute total number of members." << endl;
        cout << "4. Display members." << endl;
        cout << "PRESS 0 TO EXIT." << endl;
        cout << "-> ";
        int op;
        cin >> op;
        if (op == 0) {
            break;
        }
        else if (op == 1){
            cout << "Enter PRN: ";
            cin >> prn;
            cout << "Enter Name: ";
            cin >> name;
            insert (president, prn, name);
        }
        else if (op == 2){
            string value;
            cout << "Enter PRN or Name: ";
            cin >> value;
            Delete(president, value);
        }
        else if (op == 3){
            cout << totalMembers(president) << endl;
        }
        else if (op == 4) {
            display(president);
        }
        else {
            cout << "Wrong input!\n";
        }
    }

    

    return 0;
}
 = new Node();
    temp = first;
    while (temp != NULL) {
        if (temp -> next -> next != NULL) {
            temp = temp -> next;
        }
        temp -> next = NULL;
    }

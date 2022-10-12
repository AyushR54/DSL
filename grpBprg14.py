def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        index = i
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                index = j
        temp = arr[index]
        arr[index] = arr[i]
        arr[i] = temp
    return arr


def bubbleSort(arr):
    print()


percentage = []
n = int(input("Enter no.of students: "))
print("Enter percentage")
for i in range(n):
    score = float(input())
    percentage.append(score)

print()
print("SELECT FROM THE GIVEN OPTIONS")
print()
while(True):
    ch = int(input("1. Selection Sort\n"
                   "2. Bubble sort\n"
                   "3. Display top 5 scores"
                   "PRESS 0 TO EXIT"))
    if ch == 0:
        exit()
    elif ch == 1:
        selectionSort(percentage)
    elif ch == 2:
        bubbleSort(percentage)
    else:
        print("Please select from the given options\n\n")

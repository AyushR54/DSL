def average(n, mks):
    sum = 0
    for i in range(n):
        sum += mks[i]
    avg = sum / n
    print("Average score =", avg)


def highestLowest(n, mks):
    high = 0
    low = 100
    for i in range(n):
        if mks[i] > high:
            high = mks[i]
    for i in range(n):
        if mks[i] < low:
            low = mks[i]
    print("Highest marks =", high)
    print("Lowest marks =", low)


def absent(total, present):
    abs = total - present
    print("Absent students =", abs)


def highestFrequency(n, mks):
    max = 1
    count = 0
    for i in range(n):
        mks[i]
        for j in range(n):
            if mks[j] == mks[i]:
                count += 1
        if count > max :
            max = count
            ans = mks[i]
        count = 0
    print("Score with highest frequency =", ans)
    


total = int(input("Enter total number of students = "))
n = int(input("Enter number of students present = "))
marks = []
print("Enter marks out of 100:")
for i in range(n):
    mks = int(input("-> "))
    marks.append(mks)

print("CHOOSE FROM THE GIVEN OPTIONS")
while True:
    print()
    op = int(input("1.The average score of class\n"
                   "2.Highest score and lowest score of class\n"
                   "3.Count of students who were absent for the test\n"
                   "4.Display mark with highest frequency\n"
                   "Press 0 to exit\n"))    
    if op == 1:
        average(n, marks)
    elif op == 2:
        highestLowest(n, marks)
    elif op == 3:
        absent(total, n)
    elif op == 4:
        highestFrequency(n, marks)
    elif op == 0:
        exit()
    else:
        print("Wrong input!")

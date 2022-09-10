def cricketBadminton(cricket, badminton):
    count = 0
    '''Common names in lists'''
    for a in range(len(cricket)):
        cricket[a]
        for b in range(len(badminton)):
            if badminton[b] == cricket[a]:
                count += 1

    print("Students playing cricket and badminton =", count)



def eitherCricOrBad(cricket, badminton):
    count = 0
    '''for uncommon names in two lists'''
    for a in range(len(cricket)):
        cricket[a]
        for b in range(len(badminton)):
            if badminton[b] == cricket[a]:
                count += 1
    '''count is multiplied by two as two lists will have one common name twice'''
    ans = (len(cricket) + len(badminton)) - (2 * count)
    print("Students playing either cricket or badminton =", ans)



def neitherCricNorBad(cricket, badminton, total):
    count = 0
    for a in range(len(cricket)):
        cricket[a]
        for b in range(len(badminton)):
            if badminton[b] == cricket[a]:
                count += 1

    either = (len(cricket) + len(badminton)) - (2 * count)
    neither = len(total) - (either + count)
    print("Students playing neither cricket nor football =", neither)



def CBnotFootball(cricket, badminton, football):
    '''cricket, football and badminton'''
    cfb = 0     
    '''cricket and football'''
    cf = 0

    clen = len(cricket)
    blen = len(badminton)
    flen = len(football)

    for a in range(clen):
        cricket[a]
        for b in range(blen):
            if cricket[a] == badminton[b]:
                for c in range(flen):
                    if badminton[b] == football[c]:
                        cfb += 1

    for a in range(clen):
        cricket[a]
        for b in range(flen):
            if cricket[a] == football[b]:
                cf += 1

    ans = cf - cfb
    print("Students playing cricket and football but not badminton =", abs(ans))



total = []
n = int(input("Enter total number of students = "))
print("Enter their names/roll calls : ")
for i in range(n):
    name = input()
    total.append(name)
print(total)
print()


cricket = []
cric = int(input("Enter no. of students playing cricket = "))
print("Enter their names/roll calls : ")
for i in range(cric):
    name = input()
    cricket.append(name)
print(cricket)
print()


badminton = []
badm = int(input("Enter no. of students playing badminton = "))
print("Enter their names/roll calls : ")
for i in range(badm):
    name = input()
    badminton.append(name)
print(badminton)
print()


football = []
fb = int(input("Enter no. of students playing football = "))
print("Enter their names/roll calls : ")
for i in range(fb):
    name = input()
    football.append(name)
print(football)
print()


print("SELECT FROM THE FOLLOWING OPTIONS:")

while True:
    print()
    op = int(input("1.List of students who play both cricket and badminton\n"
       "2.List of students who play either cricket or badminton but not both \n"
       "3.Number of students who play neither cricket nor badminton\n"
       "4.Number of students who play cricket and football but not badminton\n"
       "Press 0 to exit\n"))
    if op == 1:
        cricketBadminton(cricket, badminton)
    elif op == 2:
        eitherCricOrBad(cricket, badminton)
    elif op == 3:
        neitherCricNorBad(cricket, badminton, total)
    elif op == 4:
        CBnotFootball(cricket, badminton, football)
    elif op == 0:
        exit()
    else:
        print("Wrong input!")

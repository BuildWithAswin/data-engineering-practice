# Qestion 1-> problem stmnt : find the number at a given position
# if location of element is row 5 and column 3
# ncr 4C3 of (r-1)/(c-1) = 4!/3!* (4-3)! - > 6
# so the element at location r 5 and c 3 in a pascals triangle is 6

def NcR(n, r):
    res = 1
    for i in range(0, r):
        res = res * (n-i)
        res = res // (i+1)
    return res

# print(NcR(4, 2))

# Question 2->print nth row in pascals triangle


# n = 5
# for i in range(0, n):
#    print(NcR(4, i), end="  ")
# print()


# Question 3->print pascals triangle for given n rows

# def pascals_full(n):
#    ans = []
#    for row in range(1, n):
#        templist = []
#        for col in range(1, row):
#            templist.append(NcR(row - 1, col - 1))
#        ans.append(templist)
#    return ans
#
#
# print(pascals_full(5), end="\n")


# Question 4->printa pascal trianlge for N rows:

def generaterows(row):
    ans = 1
    ansRow = []
    ansRow.insert(0, 1)
    for col in range(1, row):
        ans = ans * (row - col)
        ans = ans // (col)
        ansRow.append(ans)
    return ansRow


def pascals_triangle(N):
    ansRows = []
    for i in range(1, N+1):
        ansRows.append(generaterows(i))
    return ansRows


print(pascals_triangle(5))

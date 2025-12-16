
""" this pattern has following sections 
    1.border of zeros
    2.upper half deacreasing 654321
    3. lower half increasing 123456
    4. left and right mirroring 
"""
""" Border of zeros

Upper half (i ≤ n)

Left → Section-1 (decreasing)

Right → Section-2 (decreasing, mirrored)

Lower half (i > n)

Left → Section-3 (increasing)

Right → Section-4 (increasing """


# section 1 not proper 

n = 6

total_rows = 2 * n

# TOP ZERO BORDER
print("0 " * (2*n + 3))

for row in range(1, total_rows + 1):

    print("0", end=" ")   # left border

    #  UPPER HALF
    if row <= n:
        i = row

        # SECTION 1 (upper-left)
        for j in range(1, n+1):
            if j <= n - i + 1:
                print(n - j + 1, end=" ")
            else:
                print(" ", end=" ")

        print(" ", end=" ")  # center gap

        # SECTION 2 (upper-right)
        for j in range(1, n + 1):
            if j >= n - i + 1:
                print(i - (j - (n - i + 1)), end=" ")
            else:
                print(" ", end=" ")

    # LOWER HALF
    else:
        i = total_rows - row + 1

        # SECTION 3 (lower-left)
        for j in range(1, n + 1):
            if j <= i:
                print(j, end=" ")
            else:
                print(" ", end=" ")

        print(" ", end=" ")   # center gap

        # SECTION 4 (lower-right)
        for j in range(1, n + 1):
            if j <= n - i + 1:
                print(j, end=" ")
            else:
                print(" ", end=" ")

    print("0")   # right border

# BOTTOM ZERO BORDER
print("0 " * (2*n + 3))



#  section 4
# n = 6

# for i in range(1, n + 1):      # rows
#     for j in range(1, i + 1):  # values
#         print(j, end=" ")
#     print()


# section 3
# n = 6

# for i in range(n, 0, -1):      # rows: 6 → 1
#     for j in range(1, i+1):    # values: 1 → i
#         print(j, end=" ")
#     print()


# section 2
# n = 6

# for i in range(1, n+1):
#     for j in range(1, n+1):

#         if j >= n - i + 1:
#             print(i - (j - (n - i + 1)), end=" ")
#         else:
#             print(" ", end=" ")

#     print()


# section 1
# n = 6

# for i in range(1, n+1):        # rows
#     for j in range(1, n+1):    # columns

#         if j <= n - i + 1:
#             print(n - i-j + 2, end=" ")
#         else:
#             print(" ", end=" ")
    
    

#     print() 


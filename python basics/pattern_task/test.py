# section 1
n = 6

# for i in range(1, n+1):        # rows
#     for j in range(1, n+1):    # columns

#         if j <= n - i + 1:
#             print(n - i-j + 2, end=" ")
#         else:
#             print(" ", end=" ")
    
    

#     print() 

for i in range(1,n+1):

    for j in range(1, n + 1):
            if j < i:
                print(" ", end=" ")
            else:
                print(n - (j - i), end=" ")

    print(" ", end=" ")   # center gap
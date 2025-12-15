
""" this pattern has following sections 
    1.border of zeros
    2.upper half deacreasing 654321
    3. lower half increasing 123456
    4. left and right mirroring 
"""

n= 6

for i in range(2*n+1):  # for rows
    for j in range(2*n+1): # for column

        # step 1
        # for border of zero 
        #  taking i==0 as firs row (top border)
        # i=2*n last row(bottom)
        # j==0 fist column (left border)
        # j=2*n last column (right border)

        if i==0 or j==0 or i==2*n or j==2*n:
            print(0, end=" ")

        
        # step 2 upper half 
        else:
            #  for upper i as rows less than = n
            if i <=n: 
                
                # left traingle decreasing value 
                if j<=i:
                    print(n-j+1, end=" ")

                    # right triangle increasing value 
                elif j>=2*n-i:
                    print(j-n,end=" ")

                #  middle empty space 
                else:
                    print(" ", end=" ")
            
            # step 3 lower half
            else:
                #  left trangle deacreasing value 
                if j<=2*n-i:
                    print(n-j+1, end=" ")
                #  right triangle 
                elif j>=i:
                    print(j-n, end=" ")
                else:
                    print(" ", end=" ")
            
    print()
       

  

# time started at 10:48 to 11:44

# fibonaaci series of n terms 
# n is the number of sequence , the series will be created 
# the values must be less or equals to the n

n= 10 # 10 times the sequence will be generated

a,b = 0,1 # a and b are values to create the fibonacci sequence

i= 0 # i variable used to iterate the loop for thesequence

# a empty fibonaaci serires 

fibonaaci_numbers=[]

# starting the loop 
for i in range(n):
    if i<=n:    #tatisfies the condition 
        fibonaaci_numbers.append(str(a))# this appends the the variable a values to the list 
        # the formula for fibonacci series 
        a,b=b ,b+a
print((fibonaaci_numbers))



    
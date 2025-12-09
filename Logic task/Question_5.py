
# started at 11:45 to 1:27

# program to create list of temperature that returns number of days to wait for a warmer temperature 

# list of temperatures 

temperatures=[30,31,29,32]
def temperature_days(temperatures):

    indices_temp=[] # empty list that stores the indexes of temperature 

    result=[0] * len(temperatures) 
    # the result list will contain the number of days same as temperature list size 

    for i in range(len(temperatures)):

        while indices_temp and temperatures[i] > temperatures[indices_temp[-1]]:
            # Calculate days to wait and store in result     
                indices_temp.append(i)  

    return result


print(f"the warmer days to wait{temperature_days:} for the temperatures{temperatures}")

    

    


    

    
    
    



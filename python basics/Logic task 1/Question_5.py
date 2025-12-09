
# started at 11:45 to 1:27

# program to create list of temperature that returns number of days to wait for a warmer temperature 

# list of temperatures 

temperatures=[30,19,20,32]
def temperature_days(temperatures):

    indices_temp=[] # empty list that stores the indices of temperatures list

    result=[0] * len(temperatures) 
    # the result list will contain the number of days same as temperature list size 

    for i in range(len(temperatures)):

        #the following loop tries to access the last element through indices_temp[-1]
        # temp[i]= current days warmer than the last recorded prev day temp
        # temp[-1] is the last day temp who is at the top of indices_temp 

        while indices_temp and temperatures[i] > temperatures[indices_temp[-1]]:

            # we need to pop the elment because it has the future previous day temp
            prev_day= indices_temp.pop()
            # formula to count the days to wait
            result[prev_day]= i- prev_day 

         
        indices_temp.append(i)  # for future comparision we append the i as current day temp

    return result

days_to_wait= temperature_days(temperatures)

print(f"the warmers days to wait for the temperature{temperatures} are: {days_to_wait}")

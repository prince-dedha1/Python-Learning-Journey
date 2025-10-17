''' Create a python program capable of greeting you with Good Morning, Good Afternoon 
and Good Evening. Your program should use time module to get the current hour. 
Here is a sample program and documentation link for you: '''

import time 
local_time=time.localtime()
formated_time=time.strftime("%H:%M:%S",local_time)
if "05:00:00" <= formated_time < "12:00:00":
        print(" GOOD MORNING SIR ")
elif "12:00:00" <= formated_time < "17:00:00":
        print(" GOOD AFTERNOON SIR ")
elif "17:00:00" <= formated_time < "21:00:00":
        print(" GOOD EVENING SIR ")
else:
    print(" GOOD NIGHT SIR ")
print("CURRENT TIME IS--->  ",formated_time)
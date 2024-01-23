"""
Create 3 variables 1) swimming 2) cycling 3) running
Ask user to input times for each variable, in minutes
Add the 3 variables together to create a triathlon variable (in minutes)

To qualify for an award
0 - 100 minutes = Provincial Colours
101 - 105 minutes = Provincial Half Colours
106 - 110 minutes = Provincial Scroll
111+ minutes = No award

Stop
"""
swimming = int(input("Please enter the time it took you to complete your swim (in minutes)"))
cycling = int(input("Please enter the time it took you to cycle (in minutes)"))        
running = int(input("Please enter the time it took you to run (in minutes)"))

qualifying_time = swimming + cycling + running

if qualifying_time <= 100:
    print("Congratulations, you have won the Provincial Colours award!")
elif qualifying_time <= 105:
    print("Congratulations, you have won the Provincial Half Colours award!")
elif qualifying_time <= 110:
    print("Congratulations, you have won the Provincial Scroll award!")          
else:
    print("Sadly, you have not qualified for an award. Please try again next year.")

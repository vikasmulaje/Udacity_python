import time 
import os

work_time=int(input("enter how much time you want to work in minutes"))

ok_time=time.ctime()
print(ok_time.split()[3].split(":"))
print("So now time is ")
print(ok_time.split()[3].split(":"))
print("You will work upto")
def calculate_hours_minutes(work_time):
    hrs=work_time//60
    minutes=work_time-hrs*60
    print(hrs,minutes)
    
#print(int(ok_time.split()[3].split(":")[0])
calculate_hours_minutes(work_time)

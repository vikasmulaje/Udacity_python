import time 
import os

work_time=int(input("enter how much time you want to work in minutes:-"))

ok_time=time.ctime()
print(ok_time.split()[3].split(":"))
print("So now time is ")
current_time=ok_time.split()[3].split(":")
os.system("espeak "+current_time[0]+","+current_time[1])
print(current_time[0],current_time[1])
print("You will work upto")
def calculate_hours_minutes(work_time):
    hrs=work_time//60
    minutes=work_time-hrs*60
    return hrs,minutes
    
#print(int(ok_time.split()[3].split(":")[0])
def calculate_final_time():
    hrs,minutes=calculate_hours_minutes(work_time)
    if int(current_time[1])+minutes>60:
        print(int(current_time[0])+hrs+1,int(current_time[1])+minutes-60)
        os.system("espeak "+str(int(current_time[0])+hrs+1)+","+str(int(current_time[1])+minutes-60))
    else:
        print(int(current_time[0])+hrs,int(current_time[1])+minutes)
        os.system("espeak "+str(int(current_time[0])+hrs)+","+str(int(current_time[1])+minutes))
calculate_final_time()

def waiting_time():
    print("Waiting for "+str(work_time)+" minutes")
    time.sleep(work_time*60)
    os.system("notify-send 'you can take a break now'")
    os.system("espeak you can take a break now")
waiting_time()


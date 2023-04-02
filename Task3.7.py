# Task3.7 "Time"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 19.02.2023

t1_h = int(input("Please,input time #1 in hours <24: "))
t1_m = int(input("Please,input time #1 in minutes <60: "))
t1_s = int(input("Please,input time #1 in seconds <60: "))
t2_h = int(input("Please,input time #1 in hours <24: "))
t2_m = int(input("Please,input time #1 in minutes <60: "))
t2_s = int(input("Please,input time #1 in seconds <60: "))

time_interval = abs(t2_h * 3600 + t2_m * 60 + t2_s - (t1_h * 3600 + t1_m * 60 + t1_s))

print("Time interval between time#1 and time#2 is {} seconds!".format(time_interval))

# Task5.1 "Time"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 21.02.2023

t_hours = int(input("Please,input number of hours <24: "))
t_m = int(input("Please,input number of minutes <60: "))
t_s = int(input("Please,input number of seconds <60: "))

q_minutes = t_hours * 60 + t_m
q_seconds = t_hours * 3600 + t_m * 60 + t_s

print(f"\nSince the beginning of day has passed \n {t_hours} hours, \n {q_minutes} minutes, \n {q_seconds} seconds")
# Task3.6 "Biker"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 18.02.2023

d = 56  # distance, km
mark = 0  # km

v = float(input("Please,input biker speed: "))
t = float(input("Please,input biker time: "))

if v > 1000 or v < -1000 or t > 1000 or t < 0:
    print("Error! Input a correct speed and time!")
else:
    mark = (v * t) % d  # mark = (v * t - ((v * t) // d)*d)

print("\n You stopped at the mark", mark, "km")

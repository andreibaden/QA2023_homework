# Task3 "Squirrels and nuts"
#
# Version: 2.0
# Author: Nedaboi Andrei_QA2023
# Date: 05.02.2023

n_sq = int(input("Input the number squirrels: "))
k_nut = int(input("Input the number nuts: "))

k_nut_P = int(k_nut / n_sq)  # the number of nuts in each squirrel

print("\n The number of nuts in each squirrel = ", k_nut_P,
      "\n There are nuts left = ", k_nut - k_nut_P * n_sq)

# Task2 "a file size"
#
# Version: 2.0
# Author: Nedaboi Andrei_QA2023
# Date: 05.02.2023

file_s_byte = float(input("Input the file size on bytes: "))

file_s_kb = file_s_byte / 1024  # the file size on Kb
file_s_mb = file_s_kb / 1024  # the file size on Mb
file_s_tb = file_s_mb / 1024  # the file size on Tb

print("\n The file size on Kb = ", file_s_kb,
      "\n The file size on Mb = ", file_s_mb,
      "\n The file size on Tb = ", file_s_tb)

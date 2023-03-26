# Task1 "mass Dino"
# Version: 2.0
# Author: Nedaboi Andrei_QA2023
# Date: 05.02.2023


m_dino = float(input("Input the mass Dino in grams: "))

m_dino_kg = m_dino / 1000  # mass Dino in kilograms
m_dino_cen = m_dino_kg / 100  # mass Dino in centners
m_dino_ton = m_dino_cen / 10  # mass Dino in tons

print("\n Mass Dino in kilograms =", m_dino_kg,
      "\n Mass Dino in centners =", m_dino_cen,
      "\n Mass Dino in tons =", m_dino_ton)

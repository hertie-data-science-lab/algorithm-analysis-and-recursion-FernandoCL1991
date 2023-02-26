# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 08:24:20 2023

@author: Fernando Corral Lozada and Danial Riaz
"""

if __name__ == "__main__":

    # Move/print function
    def move(from_rod, to_rod):
        print(f"Move disc from {from_rod} to {to_rod}")

    # Recursion function
    def TowerOfHanoi(n, from_rod, aux_rod, to_rod):
        if n == 0:
            pass
        else:
            TowerOfHanoi(n-1, from_rod, to_rod, aux_rod)
            move(from_rod, to_rod)
            TowerOfHanoi(n-1, aux_rod, from_rod, to_rod)

print("Welcome to Tower of Hanoi!")
n = int(input("Enter how many disks you want to play with: "))
TowerOfHanoi(n, "A", "B", "C")

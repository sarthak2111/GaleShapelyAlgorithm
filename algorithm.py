#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: SarthakMishra
''' --- Input values --- '''
D = [
    [2, 1, 4, 5, 3],  # Department preference list
    [4, 2, 1, 3, 5],
    [2, 5, 3, 4, 1],
    [1, 4, 3, 2, 5],
    [2, 4, 1, 5, 3]
]

P = [
    [5, 1, 2, 4, 3],  # Programmer preference list
    [3, 2, 4, 1, 5],
    [2, 3, 4, 5, 1],
    [1, 5, 4, 3, 2],
    [4, 2, 5, 3, 1]
]

un_matched_programmers = {1, 2, 3, 4, 5}
un_matched_departments = {1, 2, 3, 4, 5}

# Initial matches
programmer_match = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1}
department_match = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1}

N = 5

while un_matched_programmers:
    print("Current unmatched programmers: ", un_matched_programmers)
    programmer = un_matched_programmers.pop()  # Pick an unmatched programmer
    print(f"Finding Department match for programmer: {programmer}")
    print("Programmer's preference list:", P[programmer - 1])

    # Try to find a match for the programmer
    for dept in P[programmer - 1]:
        print(f"Checking department: {dept}")

        if dept in un_matched_departments:
            # If the department is unmatched, make the match
            programmer_match[programmer] = dept
            department_match[dept] = programmer
            un_matched_departments.remove(dept)
            print(f"Programmer {programmer} matched with Department {dept}")
            print("-------------------------------------------------------------------------------------------------------------\n")
            break
        else:
            # If the department is already matched, check if the department prefers this programmer
            current_programmer = department_match[dept]
            if D[dept - 1].index(programmer) < D[dept - 1].index(current_programmer):
                # Department prefers the new programmer
                print(f"Department {dept} prefers Programmer {programmer} over Programmer {current_programmer}")

                # Unmatch the current programmer and match the new one
                programmer_match[current_programmer] = -1
                un_matched_programmers.add(current_programmer)

                programmer_match[programmer] = dept
                department_match[dept] = programmer
                print(f"Programmer {programmer} matched with Department {dept}")
                print("-------------------------------------------------------------------------------------------------------------\n")
                break

''' --- Visualizing the result, Printing the output --- '''
Names = [
    ['HR', 'CRM', 'Admin', 'Research', 'Development'],  # Department names
    ['Adam', 'Bob', 'Clare', 'Diane', 'Emily']           # Employee names
]

print('Result is:-')
# Map the result to the names

for i in range(N):
    print(Names[0][i], ":", Names[1][programmer_match[i+1] - 1]) # Map the result to the names


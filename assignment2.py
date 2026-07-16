#!/usr/bin/env python3

'''
OPS445 Assignment 2 - Winter 2023
Program: assignment2.py 
Author: "Jyotirth Oza"
The python code in this file is original work written by
Jyotirth Oza. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: <Enter your documentation here>

Date: 

'''

def percent_to_graph(percent, total_chars):
    """Return a graph made of hash symbols and spaces."""
    hash_count = int(percent * total_chars)
    space_count = total_chars - hash_count

    return "#" * hash_count + " " * space_count


def get_sys_mem():
    """Return the total system memory in KiB."""
    with open("/proc/meminfo", "r") as mem_file:
        for line in mem_file:
            if line.startswith("MemTotal:"):
                return int(line.split()[1])

    return 0


def get_avail_mem():
    """Return the available system memory in KiB."""
    with open("/proc/meminfo", "r") as mem_file:
        for line in mem_file:
            if line.startswith("MemAvailable:"):
                return int(line.split()[1])

    return 0
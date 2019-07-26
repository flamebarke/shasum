#!/usr/bin/python3

# Import required modules
import sys
import os
from sys import argv

# Define Colors
CRED = '\033[91m'     
CREND = '\033[0m'
CYEL = '\033[33m'
CYEND = '\033[0m'
CGRE = '\33[92m'
CGEND = '\33[0m'

# Function to check required # of arguments have been provided
def error():            
    if len(sys.argv) < 3:
        print(CRED + f"\nERROR NOT ENOUGH ARGUMENTS!" + CREND)
        print(CYEL + f"\nUSAGE: \tpython3 ./shasum.py [ALGORITHIM] [FILE]" + CYEND)
        print(CYEL + f"\nALGORITHIMS: 1, 224, 256, 384, 512, 512224, 512256\n" + CYEND)
        sys.exit(1)

# Run error function
error()

# Define arguments
script,algorithm,file = argv

# Main function = compares shasums
def shasum():
    os.system("shasum --algorith " + f"{algorithm} " + f"{file}" + " | cut -d' ' -f1 > shasum")
    with open('shasum', 'r') as f:
        for line in f:
            line = line.rstrip()
            print(f"\n{line}")
        
    sha_txt = input(CYEL + "\nEnter the sha checksum provided from the source >: \n\n" + CYEND)
    if line == sha_txt:
        print(CGRE + "\nSHASUM matches -- File integrity is OK!\n" + CGEND)
        exit(0)
    else:
        print(CRED + "\nSHASUM does not match -- File is modified!\n" + CREND)
        exit(0)

# Run main function
shasum()

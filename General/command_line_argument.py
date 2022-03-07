import sys

WORDS_FILE = "words.txt"

print(sys.argv)
print()

# Ensure that the program has the correct number of command line arguments
if len(sys.argv) != 2:
    print("One command line argument must be provided.")
    print("Quitting...")
    quit()

# Open the file. Quit if the file 
# is not opened successfully.
try:
    inf = open(sys.argv[1], "r")
except:
    print("Failed to open ’%s’ for reading. Quitting..." % \
        sys.argv[1])
    quit()



import sys

WORDS_FILE = "words.txt"

# Open the file. Quit if the file 
# is not opened successfully.
try:
    inf = open(sys.argv[1], "r")
except:
    print("Argument file missing")
    print("Please provide the input file to process")
    quit()

# Load all of the words into a dictionary of valid words. The value 0 is associated with each
# word, but it is never used.

valid = {}
words_file = open(WORDS_FILE, "r")

for word in words_file:
    # Convert the word to lowercase and remove
    # the trailing newline character

    word = word.lower().rstrip()
    # Add the word to the dictionary
    valid[word] = 0

words_file.close()
print(len(valid))

# Read each line from the file, adding any misspelled words to the list of misspellings
misspelled = []
for line in inf:
    words = line.split(' ')
    for word in words:
        # Only add to the misspelled list 
        # if the word is misspelled and not already in the list
        if word.lower() not in valid and word not in misspelled:
            misspelled.append(word)

print(misspelled)

# Close the file being checked
inf.close()

# Display the misspelled words, 
# or a message indicating that no words are misspelled

if len(misspelled) == 0:
    print("No words were misspelled.")
else:
    print("The following words are misspelled:")
    for i in range(len(misspelled)):
        print(i, misspelled[i])
        





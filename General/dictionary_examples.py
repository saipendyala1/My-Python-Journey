
# tel = {'jack': 4098, 'sape': 4139}
# print(tel)
# tel['guido'] = 4127
# print(tel)

# for key, value in tel.items():
#     print(key, value)


import re
import random

path = 'D://Documents//UoL//COMP517_Programming_Fundamentals//week_4//'

reviews = {}
with open(path+'goldfinch.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    for line in content:
        #print(line)
        line = re.sub('\n', '', line)
        split_line = line.split('\t')
        #print(len(split_line))
        score, review_id, title, review = split_line[0], split_line[1], split_line[2], split_line[3]  
        reviews[review_id] = {"score" : score, "title" : title, "review" : review}
        
# Take a random key from the dictionary and print its value
# print(reviews[random.choice(list(reviews.keys()))])

# Counting the number of lines in the file
print("Number of lines: " + str(len(content)))

# # Counting the keys in the dictionary; should equal the number of lines in the file
print("Number of dictionary keys: " + str(len(reviews.keys())))


# Filter Dictionary
# Store review keys with low score (1.0) in list
lowScoreReviews = []
for key, value in reviews.items():
    if float(value["score"]) == 1.0: # Convert score to float
        lowScoreReviews.append(key)
print(len(lowScoreReviews))



# print(len(lowScoreReviews))
# # Print all the entries with a low review score
# #for item in lowScoreReviews:
#     #print(reviews[item])
# print()
# print(lowScoreReviews[0])


# List comprehension to get a subset dictionary. Alternatively you can use `.pop` instead of `.get`
dictcomp = {k : reviews.get(k) for k in lowScoreReviews}

print(lowScoreReviews[0])
print(reviews.get(lowScoreReviews[0]))



# Rearrange dictionary
from collections import defaultdict

scoredict = defaultdict(list)
# scoredict = {}

# for key, value in reviews.items():
#     print()
#     print(key)
#     print(value)
#     print(df)
#     newvalues = {'id' : key, "title" : value['title'], "review" : value['review']}
#     if value['score'] in scoredict:
#         scoredict[value['score']].append(newvalues)
#     else:
#         scoredict[value['score']] = []
#         scoredict[value['score']].append(newvalues)


for key, value in reviews.items():
  newvalues = {'id' : key, "title" : value['title'], "review" : value['review']}
  # Use the 'score' from the values (!) in the original dictionary as the key for the newly created dictionary
  scoredict[value['score']].append(newvalues)
  
# Print the dictionary keys to verify that these are indeed review scores
print(scoredict.keys())

for key, value in scoredict.items():
    print(key, len(value))



# import re
# # Import defaultdict
from collections import defaultdict

freqDict = defaultdict(int)
for item in lowScoreReviews:
    review = reviews[item]["review"]
    cleantext = re.sub(r'<.*?>', '', review).strip().split() # Remove HTML tags and split the review by word (space separated)
    for word in cleantext:
        # Convert to all lowercase
        word = word.lower()
        
        # Complete the following line to increase the count by one:
        # were
        # {'were': 0}
        freqDict[word] += 1
        # {'were': 1}

print(freqDict)


# import collections

# print('Regular dictionary:')
# d = {}
# d['a'] = 'A'
# d['b'] = 'B'
# d['c'] = 'C'

# for k, v in d.items():
#     print(k, v)

# print('\nOrderedDict:')
# d = collections.OrderedDict()
# d['a'] = 'A'
# d['b'] = 'B'
# d['c'] = 'C'

# for k, v in d.items():
#     print(k, v)    


# from collections import OrderedDict

# # Create Ordered dictionary
# ordDict = OrderedDict(sorted(freqDict.items(), key=lambda item: item[1], reverse=True))

# print(ordDict)

# # Ignore top 10%
# top10 = int(len(ordDict.keys())/10)

# # Print 100 words of the top 90%
# print(list(ordDict.items())[top10:top10+100])




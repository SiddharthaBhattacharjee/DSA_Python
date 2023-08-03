"""__ProblemStatement__:
        poem.txt Contains famous poem "Road not taken" by poet Robert Frost. 
        You have to read this file in python and print every word and its count as show below. 
        Think about the best data structure that you can use to solve this problem,
        and figure out why you selected that specific data structure.
"""

Occurence = {}

with open('./Exercise_problems/assets/poem.txt','r') as txt:
    for line in txt:
        for word in line.split():
            if word in Occurence.keys():
                Occurence[word] += 1
                continue
            Occurence[word] = 1

print(Occurence)
from collections import Counter
liste = [2, 3, 2, 4, 5, 3, 7, 3, 8, 9, 2, 4, 1, 5, 7, 5]
#makes a dictionary with most occurences first
counts_dict = Counter(liste)
#returns the first key of the dictionary
print(list(counts_dict.keys())[0])

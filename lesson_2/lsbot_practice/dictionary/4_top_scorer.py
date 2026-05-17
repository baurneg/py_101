# 4. Find Top Scorer

# •   ​Difficulty​: Advanced
# •   ​Description​: Write a function find_top_scorer that takes a dictionary 
# of player scores. The function should return the name (key) of the player 
# with the highest score. If the dictionary is empty, it should return None.
# [8:40 PM]If there's a tie for the highest score, returning any one of the 
# top scorers is acceptable.

def find_top_scorer(d):
    


#     ​Test Cases:

scores1 = {'Alice': 88, 'Bob': 92, 'Charlie': 92, 'David': 75}
print(find_top_scorer(scores1))
# Expected output: 'Bob' or 'Charlie'

scores2 = {'Physics': 95, 'Chemistry': 98, 'Math': 95}
print(find_top_scorer(scores2))
# Expected output: 'Chemistry'

print(find_top_scorer({}))
# Expected output: None
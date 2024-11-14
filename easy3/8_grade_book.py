# Write a function that determines the mean (average) of the three scores 
# passed to it, and returns the letter associated with that grade.

# Numerical score letter grade list:

# 90 <= score <= 100: 'A'
# 80 <= score < 90: 'B'
# 70 <= score < 80: 'C'
# 60 <= score < 70: 'D'
# 0 <= score < 60: 'F'
# Tested values are all between 0 and 100. There is no need to check for 
# negative values or values greater than 100.

# ExamplesCopy Code
# print(get_grade(95, 90, 93) == "A")      # True
# print(get_grade(50, 50, 95) == "D")      # True

def get_grade(grade_1, grade_2, grade_3):
    average_score = (grade_1 + grade_2 + grade_3) / 3
    if average_score >= 90:
        return 'A'
    elif 80 <= average_score < 90:
        return 'B'
    elif 70 <= average_score < 80:
        return 'C'
    elif 60 <= average_score < 70:
        return 'D'
    else:
        return 'F'
print(get_grade(95, 90, 93) == "A")
print(get_grade(50, 50, 95) == "D") 
print(get_grade(20, 30, 55) == "F")
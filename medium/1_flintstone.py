# Question 1
# Let's do some "ASCII Art": a stone-age form of nerd 
# artwork from back in the days before computers had 
# video screens.
# For this practice problem, write a program that 
# outputs The Flintstones Rock! 10 times, with each 
# line prefixed by one more hyphen than the line above 
# it. The output should start out like this:
# € Copy Code
# -The Flintstones Rock!
# --The Flintstones Rock!
# ---The Flintstones Rock!

text = 'The Flintstones Rock!'
for i in range(1,11):
    print(('-' * i) + text)

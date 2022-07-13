# def a string variable
course = "Python's Course for Beginners"
print(course)
# def a multiple line string
multi_line = '''
Hi Raj,

Here is our first email to you.

Thankyou.
'''
print(multi_line)
# Print first character of a string
print(course[0])
# Print last character of a string
print(course[-1]) #Note: Negative indexing not available in other languages
# Print first 3 characters of course [0,1,2]
print(course[0:3])
# Copy content of 1 variable to another
another_course = course[:]
# Print
print(another_course)
# Copy partial content of 1 variable to another
another_variable = course[5:15]
# Print
print(another_variable)

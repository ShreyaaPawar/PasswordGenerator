import string
import random

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

s = []

s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)

user_leninput = input("Enter the length of the password you want to generate: ")

if user_leninput.isdigit():
    random.shuffle(s)
    print("".join(s[:int(user_leninput)]))

else:
    print("Wrong Input!!!!Try Again....")


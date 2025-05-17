# random password generator
import random
import string
pass_len=8
charVal= string.ascii_letters + string.digits + string.punctuation
res="".join([random.choice(charVal) for i in range(pass_len)])
print(res)
#another method
#import random
# password=""
# for i in range(pass_len):
#     password +=random.choice(charVal)
# print("your suggested pasword is:",password)
#using  list comprehension
# [function for i in range(n)]
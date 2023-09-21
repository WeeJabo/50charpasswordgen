import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!£$%^&*(){}[]~#@:¬`\|?><.,_+-="

string = lower + upper + numbers + symbols
length= 50
password = "".join(random.sample(string,length))

print("Your New Password Is : " + password)
print("             ")
print("Keep Safe!")

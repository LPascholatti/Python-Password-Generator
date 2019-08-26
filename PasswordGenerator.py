#generate a password with length "passlen" with no duplicate characters in the password

import random

print ("Welcome to Lucas Pascholatti's Password Generator, below you will find your new password: \n")

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample(s,passlen))
print (p)

print = input("\nWrite exit to leave: \n")

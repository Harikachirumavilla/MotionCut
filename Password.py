""" WELCOME TO PASSWORD GENERATE PROJECT
        BY USING PYTHON MODULES"""
#import modules
import math as m #for floor method
import random as r
#function to generate password
def password_generate():
     #declare a string variable
     #which stores alpha-numeric characters
     string='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#%^&*"'
     password=" "
     password_length=len(string)  
     for i in range(length_password):
        password+=string[m.floor(r.random()*password_length)]
     return(password)
#main function
length_password=int(input("enter the length of password:"))
no_of_passwords=int(input("enter the number of passwords to generate:"))
temp=no_of_passwords
while(no_of_passwords>0): 
  print("your one time password is",password_generate())
  no_of_passwords-=1
print("***{} PASSWORDS WERE GENERTAED SUCCESSFULLY***".format(temp))

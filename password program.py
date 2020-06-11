#this program is a test

x=1
y=1

while True:
    print('Enter your password:')
    password = input()
    if password.isdecimal():
        x=0
    if password.isalpha():
        y=0
    z=x+y
    if z == 2:
        break
            
    print('Please enter letters and numbers for your password.')
    x=1
    y=1
    

import csv

dict1 = {}

e = []

x = 0

s = 0

#13 to 90 is tally points to make sure the password is secure

def uID():
    
    s = 0
    
    while True:

        print('''Needed Points
    - At least 8 charactrers
    -Includes Uppercase
    -Includes Lowercase
    -Includes Numbers
    -Needs !, $, %, &, <, *, @''')
        
        password = input('Please select an Password: ')

        if len(password) < 8:
            
            print('Not enough words')

        else:
            s += 1
             
        if password != password.upper:

            s += 1

        else:
            print('Needs a uppercase letter')
        
                
        if password != password.lower:
            s += 1

        else:
            print('Needs a lowercase letter')
                
            
        for i in range(10):
            if str(i) in password:
                s += 1
                break

            else:
                None
                s += 1
        if '!' in password or '$' in password or '%' in password or '<' in password or '*' in password or '@' in password:
            s += 1

        else:
            print('Needs a special character')

        if s == 1 or s == 2:
            print('Weak, Recommend Changing')
            s = 0
            
        
        if s == 3 or s == 4:
            print('Can be imporved')
            s = 0
            inp = input('Would you like to change password(y/n): ')
            if inp == 'y':
                None
                #r = ('Please pick a new password: ')
            else:
                file = open('passwords1.csv','a')
                file.write(ID)
                file.write(inp)
                file.close()

        if s == 5:
            print('Strong password')
            s = 0 
            file = open('passwords1.csv','a')
            file.write(ID)
            file.write(',')
            file.write(password + '\n')
            file.close()
            break
        
    dict1[ID] = password
    return password

#Changing password

def change(uID,password,x):
    while True:

        b = input('Enter pre-excisting user ID: ') #new ID

        file = open('passwords1.csv','r')
        if b in dict1:
            password = uID()
            file = open('passwords1.csv','w')
            file.close()
            file = open('passwords1.csv','a')
            file.write(b)
            file.write(',')
            file.write(password)
            file.write('\n')
            file.close()
            break

        else:
            print('This is not a user ID that was used') 
        
file = open('passwords1.csv','w')
file.close()

while True:
    try:

        print('''Menu
        1) Create a new User ID
        2) Change a password
        3) Display all User IDs
        4) Quit''')

        start = int(input('Please select an avaliable option: '))

        if start == 1:
            while True:
                ID = input('Enter an ID: ')
                if ID in dict1:
                    print('name already used')
                if ID not in dict1:
                    dict1[ID] = ''
                    break
            
            password = uID()
            print(password)

        if start == 2:

            change(uID,password,x)

        if start == 3:
            print(dict1.keys())

        if start == 4:
            print('Have a nice day')
            break

    except:
        print('This is not an avaliable option')
        
import random
import sys
from cs50 import SQL


db = SQL("sqlite:///users.db")

def main():

    # check_arg()
    while(True):
        response = input("Want to create a new User ? :")
        if response in ['yes','yaa','yep','y']:
            user = generate_user()
            db.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                user['username'],
                user['password'],
            )

        else:
            if response in ['no','naa','nope','n']:
                print("Ok fine.Have a Nice day")
            else:
                print("please enter a valid input..such as,[yes,yaa,yep,y or no,nope,naan,n]")
            break



# def check_arg():
#     if len(sys.argv) < 1:
#         sys.exit("Too few Command-line Arguments!!")
#     if len(sys.argv) > 1:
#         sys.exit("Too many Command-line Arguments!!")




def get_dob(k):
        dob = ''
        c = k.split('/')
        if len(c) == 3:
            for i in c:
                dob = dob + i
            if len(dob) == 8:
                if 0<int(c[0])<=31 and 0<int(c[1])<=12 and int(c[2])>0:
                    return dob

        sys.exit("OPPS Something went Wrong!! Try again ")



def get_key(password,dob):

    if len(password) > len(dob):
        dif = len(password) - len(dob)
        dob = dob + dob[:dif]
    else:
        dif = len(dob) - len(password)
        dob = dob[:len(dob)-dif]

    output = dob
    return output



def encrypt(password , key):
    res = ''

    for i in range(len(key)):
        if password[i].isnumeric():
            p = int(key[i]) + int(password[i])
            res = res + str(p)
        else:
            k = int(key[i]) + int(ord(password[i]))
            res = res + chr(k)

    return res



def decrypt(enc_psd , key):
    psd = ''

    for i in range(len(enc_psd)):
        if enc_psd[i].isnumeric():
            p = int(enc_psd[i])-int(key[i])
            psd = psd + str(p)
        else:
            k = int(ord(enc_psd[i])) - int(key[i])
            psd = psd + chr(k)

    return psd



def get_password(length = 10):
    a = ''
    password = ''

    upper_letter = "ASDGFHJKLMNBVCXZQWERTYUIOP"
    lower_letter = upper_letter.lower()
    symbol = "!@#$%&*^_?.()"
    number = "0123456789"
    a = a + upper_letter + lower_letter + symbol + number

    try:
        for _ in range(int(length)):
            password = password + random.choice(a)
    except ValueError:
        sys.exit("Please Enter a Valid Number")

    return password



def generate_user():
    username = input("please enter your username: ")

    response = input("Want us to generate your password ? :")
    if response in ['yes','yaa','yep','y']:
        length = input("Please enter length of your password: ")
        password = get_password(length)
        print("your password is",password)
    else:
        password = input("please enter your password: ")

    print("please enter your DOB in DD/MM/YYYY format!!")
    k = input("your DOB: ")
    DOB = get_dob(k)
    key = get_key(password,DOB)

    en_psd = encrypt(password,key)

    return {"username":username , "password":en_psd}




if __name__ == '__main__':
    main()


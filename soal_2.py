import re

cek = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(id|co.id)+\b'

def cek_email(email):
    length=0
    for i in email:
        length+=1
        if i == '@':
            break 
    if length < 21:
        if re.match(cek, email):
            return "Email valid."
        else:
            return "Tidak Valid."
    else:
        return "Tidak Valid."

if __name__ == '__main__':
    print("Program Check Format Email")
    email = str(input("Input e-mail: "))
    print("Output: " + cek_email(email))
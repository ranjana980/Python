print("signup or login")
login=input("enter 1 for signup or enter 2 for login")
if login=="1":
    username=input("enter your name")
    f=open("login.txt","r")
    m=f.read()
    if username not in m:
        password=input("creat a password")
        m=open("login.txt","a")
        m.write("\n")
        m.write(username)
        m.write("\n")
        m.write(password)
        m.close()
        print("your acount has been created")
        f.close()
    else:
        print("username name alreday exist")
else:
    new_userinput=input("enter the name")
    file=open("login.txt","r")
    file_read=file.read()
    if new_userinput in file_read:
        new_password=input("enter the paasword")
        if new_password in file_read:
            print("login successfull")
            file.close
        else:
            print("password incorrect")
    else:
        print("username is wrong")